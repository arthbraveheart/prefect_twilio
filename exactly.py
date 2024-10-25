from prefect import task, flow
#from prefect.schedules import CronSchedule

from twilio.rest import Client

# Definindo as variáveis do Twilio
TWILIO_SID = 'AC069f1485becb681509aa3ea0b36dec02'
TWILIO_AUTH_TOKEN = '5b8babb909ba51469d44f86aa9c048c2'
TWILIO_PHONE_NUMBER = 'whatsapp:+553299696625'    #3299696625
DESTINATION_PHONE_NUMBER = 'whatsapp:+553285140754' #3285140754 #3199795243


# Twilio authentication details (use your actual credentials)
account_sid = 'AC069f1485becb681509aa3ea0b36dec02'
auth_token = '5b8babb909ba51469d44f86aa9c048c2'
twilio_number = 'whatsapp:+553299696625'  # Twilio's sandbox WhatsApp number

# Create Twilio client
client = Client(account_sid, auth_token)

# Task to send a WhatsApp message using Twilio
@task
def send_whatsapp_message(to, message_body):
    message = client.messages.create(
        from_=twilio_number,
        body=message_body,
        to=to  # Receiver's WhatsApp number (format: 'whatsapp:+1234567890')
    )
    print(f"Message sent to {to}: {message.sid}")

# Use CronSchedule to run on 2024-10-24 at 9 PM (21:00)
#schedule = "20 3 24 10 * 2024"

# Prefect flow with the scheduled date
@flow(name='sender_JJ')
def send_it():
    # Send a WhatsApp message to a specific number with a custom message
    send_whatsapp_message("whatsapp:+553285140754", "Your scheduled notification for 2024-10-24.")

# To start the flow (can also be registered with Prefect Cloud)
if __name__ == "__main__":
    send_it()#.serve(name='floshist' , cron='*/20 * * * *',)
