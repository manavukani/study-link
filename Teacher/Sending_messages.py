def send_message(message):
    from twilio.rest import Client

    client = Client("<ADD YOUR KEY>", "<ADD YOUR KEY>")

    numbers=["+919999999999","+919999999999","+919999999999","+919999999999"]
    names=["Manav","Hardeep","Utsav","Ahmed"]

    for i in range(4):
        m=("Hello {} ".format(names[i]))+message
        client.messages.create(to=numbers[i], 
                            from_="+13092711496", 
                            body=(m))

                           
