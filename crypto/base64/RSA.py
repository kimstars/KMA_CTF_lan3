from Crypto.Util.number import *
from secret import FLAG
import random

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 5

# Some random padding
def pad(msg):
    msg = msg + b"\x00" + bytes(random.choices(range(1,256),k=5))
    return bytes_to_long(msg)

if __name__ == "__main__":
    print(n)
    for i in range(2):
        plaintext = pad(FLAG)
        print(pow(plaintext,e,n))

# 25201477722938533814197591031215731465390107608306336616768265500531603563278811189404276327802947131516292816866931335155904790297059057977643866269556829989656288304162663094567090965907006869728271347920641973207726071120099217368888075576498390740994575774918218312190901555707741450722770784548069302725839025180148857687687713306288839186147208810258341274774151001255135178879634795385897899458461446065818244160649213133604558692810443881523157075705344139368004234659332584076308349913496074151312020920926759411958765070327521000837453147614946561876674808726730828340370389533458528649412653915475375525691
# 24894921617112251459874199025949498248738767640505553662218916549583102430204390610114933388140985477309064166812767325002624255705767064848909226238196654793902901181437405549883380452516410576659040860116101561989954097785073520943670893217761175966588676639213521016513352092385058300591278054677822563307880853623064621292879562795118373858181618205380392005709570767293820006160914826612168161962671707116275433609625085193486843791258801374726678569214385821939963668990023053382541252105732844685551813041779717025321564164175267317608540814915966579711450220766203435146643530159481248458169396911203138568705
# 16817667697626853676172176994943941749334591620250349819618775490712248558528663258875511216478511737306047729015069438530757395020278965635254543781511574812880541272388552195877468336248064280865139997127750722548354752606999338614950290054958377016438714477699216501269777261610515376151988876197329618491087730869191074755555655803363872549538059769662325136579875340447954185903331781003507889531584893954712806155403623142241475723837154282683067364751669105101883047651837433866288276349085879572278546734585192087324906403500701073616022537859620315875952893047925006063141768685760316196145882837837239366272