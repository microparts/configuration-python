from config_pkg import PKG

c = PKG(config_path='configuration')
c.load()
print(c.get_all())