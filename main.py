from noccelerator.configuration import Configuration
from noccelerator.xmlwriters import ConfigWriter
from noccelerator.xmlwriters import NetworkWriter

def main():
    config = Configuration()
    print(config)

    writer = ConfigWriter(config)
    writer.write_config('config.xml')

    writer = NetworkWriter(config)
    writer.write_network('network.xml')

if __name__ == '__main__':
    main()