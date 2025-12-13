import resend
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class ResendEmailBackend(BaseEmailBackend):
    """Custom email backend for Resend."""

    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently, **kwargs)
        resend.api_key = settings.RESEND_API_KEY

    def send_messages(self, email_messages):
        """Send one or more EmailMessage objects and return the number sent."""
        if not email_messages:
            return 0

        num_sent = 0
        for message in email_messages:
            try:
                params = {
                    "from": message.from_email or settings.DEFAULT_FROM_EMAIL,
                    "to": list(message.to),
                    "subject": message.subject,
                }

                # Handle HTML content
                if hasattr(message, 'alternatives') and message.alternatives:
                    for content, mimetype in message.alternatives:
                        if mimetype == 'text/html':
                            params["html"] = content
                            break
                    params["text"] = message.body
                else:
                    params["text"] = message.body

                # Add CC and BCC if present
                if message.cc:
                    params["cc"] = list(message.cc)
                if message.bcc:
                    params["bcc"] = list(message.bcc)

                # Add reply-to if present
                if message.reply_to:
                    params["reply_to"] = list(message.reply_to)

                resend.Emails.send(params)
                num_sent += 1

            except Exception as e:
                if not self.fail_silently:
                    raise
                # Log the error in production
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Failed to send email via Resend: {e}")

        return num_sent
