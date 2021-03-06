# Function VAT
def get_vat(payment, persent = 20):           #persent (процент) по умолчанию = 20
       try:
           payment = float(payment)
           vat = payment / 100 * persent
           vat = round(vat, 2)               #округляем до 2 цифр после запятой
           return 'Sum VAT: {}'.format(vat)
       except TypeError:                      #в случае ошибки
           return "Can't count. Check data!"  #пишется эта надпись
result = get_vat(400, 15)                        # Если здесь будет указан процент (2-е значение), то наверху persent не учитывается
print(result)