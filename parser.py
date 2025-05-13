import configparser

mess_config = configparser.ConfigParser()
mess_config.read('mess.ini')

prod_config = configparser.ConfigParser()
dev_config = configparser.ConfigParser()

for section in mess_config.sections():
    env = mess_config[section].get('env', None)

    cleaned_section = {k: v for k, v in mess_config[section].items() if k != 'env'}

    if env == 'prod':
        prod_config[section] = cleaned_section
    elif env == 'dev':
        dev_config[section] = cleaned_section

with open('prod_config.ini', 'w') as prod_file:
    prod_config.write(prod_file)

with open('dev_config.ini', 'w') as dev_file:
    dev_config.write(dev_file)
