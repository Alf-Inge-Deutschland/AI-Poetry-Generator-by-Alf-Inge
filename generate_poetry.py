import argparse
from poetry_model import AIPoetryGenerator

def main():
    parser = argparse.ArgumentParser(description='AI Poetry Generator')
    parser.add_argument('--style', type=str, default='free verse', help='Style of the poem (e.g., sonnet, haiku, free verse)')
    parser.add_argument('--theme', type=str, default='nature', help='Theme of the poem (e.g., love, nature, sadness)')
    args = parser.parse_args()

    generator = AIPoetryGenerator()
    poem = generator.generate_poem(style=args.style, theme=args.theme)
    print(poem)

if __name__ == "__main__":
    main()
