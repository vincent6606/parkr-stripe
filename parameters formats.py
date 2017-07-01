def create_custom_account(first_name, last_name, dob, mob, yob,
                          bank_account_num, bank_routing,
                          bank_country='CA', bank_holder=None, bank_object="bank_account", bank_currency='cad', bank_type='individual',
                          token=None, currency="cad", country="CA", ip_address='8.8.8.8'):

first_name/last name:
	string
dob:
	string "24"
mob:
	string "06"
yob:
	string "1995"

bank_account_num
	dependent on Country

bank_routing
	For Canadian accounts:
		routing number is an 8 digit routing number consisting of 5 digit branch number and a 3 digit transit number
		can be entered as "XXXXX-YYY" the dash is recognized by Stripe or "XXXXXYYY"
	For American accounts:
		routing number is a 9 digit number

bank_country/country
	a 2-letter capitalized countriy code(ISO 3166-1 alpha-2): "CA","US","UK"
	https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

bank_currency/currency
	a 3-letter lower-case currency code "cad","usd"
	http://www.xe.com/iso4217.php#A

bank_holder:
	name of the account holde it is first_name+' '+last name by default
	
bank_object="bank_account"
	always "bank_account" if using a bank account, else, use a token

ip_address
	a valid ipv4 ip address XXX.XXX.XXX.XXX like 192.168.0.1 or 8.8.8.8 in string format	