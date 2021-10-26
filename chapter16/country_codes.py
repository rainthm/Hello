import pygal.maps

def get_country_code(country_name):
    for code, name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    return None
if __name__ == '__main__':
    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('Afghanistan'))