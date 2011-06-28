import bitly
apikey = 'R_f5236a661a48b7a79555db4461d9aa9a'
api = bitly.Api(login='timparkin', apikey=apikey)
short = api.shorten('www.google.com')
print short
