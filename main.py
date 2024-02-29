import os
import yaml
from generator import Generator
from translator import translate_function

def setup():
    keys = os.path.join("keys.yaml")
    # Read in keys
    with open(keys, "r") as file:
        config = yaml.safe_load(file)
        

    generator = Generator(config)
    return config, generator


def main():
    print("Hello, to the world of translation!")
    print("let's bring people together!")
    config, generator = setup()
    
    paragraph = generator.start_conversation()
    translation = translate_function(paragraph, from_lang=config["from_lang"], to_lang=config["to_lang"])
    generator.generate_voice(translation, useEL=False)
    
if __name__ == "__main__":
    main()


    