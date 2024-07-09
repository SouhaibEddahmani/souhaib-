# TP POO n°5 :
#EXERCICE 1:
#1\ email :
import re
def email_valid(email):
    ex =r"[a-zA-Z0-9\._\+-]+@[a-z0-9]+\.[a-z]+"
    if re.match(ex, email):
        print("l email est valide")
    else:
        print("l email n est pas valide")

#2\ phone :
import re
def valider_phone(phone):
    text = r"\+212|00212|0)(5|6|7|8)[0-9]{8}"
    if re.match(text,phone):
         return true
    else:
         return false


#EXERCICE 2:
#1\ mots interdits :
import re
text ="ABCD FBTREBX CBUIBMJ KBPHGBR"
nom =re.sub(r"(abcd/efgh)","*",text)
print (nom)

#2\ carte de credit :
import re
def validate_credit_card(card_number):
 card_regex = r'^(?:\d{4}[-\s]?){3}\d{4}$|^\d{16}$'
 if re.match(card_regex, card_number):
        return True
 else:
        return False


#EXERCICE 3:
#1\ hashtags :
import re
def extract_hashtags(text):
    hashtag_regex = r'#\w+'
    hashtags = re.findall(hashtag_regex, text)
    return hashtags

#2\ mot de passe:
import re
def check_password_strength(password):
    uppercase_regex = r'[A-Z]'
    lowercase_regex = r'[a-z]'
    digit_regex = r'\d'
    special_char_regex = r'[!@#$%^&*(),.?":{}|<>]'
    if (
            len(password) >= 8 and
            re.search(uppercase_regex, password) and
            re.search(lowercase_regex, password) and
            re.search(digit_regex, password) and
            re.search(special_char_regex, password)
    ):
        return True
    else:
        return False

#EXERCVICE 4 :
#1\ URL:
import re
def validate_urls(url_list):
    regex = re.compile(r'(([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,})')
    valid_urls = []
    for url in url_list:
        if regex.match(url):
            valid_urls.append(url)
        else:
            valid_urls.append(None)
    return valid_urls

#2\ HTML :
import re
def extract_a_tags(html):
    regex = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)">(.*?)</a>', re.IGNORECASE)
    return regex.findall(html)

