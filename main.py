import smtplib
import requests
from email.mime.text import MIMEText

api_key = "e361408hgjkgjjhjlknkd5"
OWN_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

MY_EMAIL = "demo@gmail.com"
MY_PASSWORD = "epq0gbsghfhhha"

weather_params = {
    "lat": 17.725300,
    "lon": 79.154900,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWN_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        # print("Bring an umbrella.")

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        # Create the email message
        subject = "Today's Weather"
        message = "It's going to rain today. Remember to bring an ☔️."
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL

        # Send the email
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.as_string())

    print("Email sent successfully.")
else:
    print("No need to bring an umbrella.")
