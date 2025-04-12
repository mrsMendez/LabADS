from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    TWILIO_ACCOUT_SID = config('TWILIO_ACCOUT_SID')
    TWILIO_ACCOUT_TOKEN=config('TWILIO_ACCOUT_TOKEN')
    TWILIO_WHATSAPP_NUMBER = ('TWILIO_WHATSAPP_NUMBER')
    

class DevelopmentConfig(Config):
    DEBUG = True

app_config = {
    'development' : DevelopmentConfig
}