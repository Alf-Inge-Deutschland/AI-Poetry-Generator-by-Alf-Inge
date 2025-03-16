import random

class AIPoetryGenerator:
    def __init__(self):
        self.styles = {
            "sonnet": self._generate_sonnet,
            "haiku": self._generate_haiku,
            "free verse": self._generate_free_verse,
        }
        self.themes = {
            "love": ["love", "heart", "passion", "romance"],
            "nature": ["tree", "river", "mountain", "forest"],
            "sadness": ["tears", "pain", "sorrow", "grief"],
        }

    def generate_poem(self, style="free verse", theme="nature"):
        if style not in self.styles:
            style = "free verse"
        if theme not in self.themes:
            theme = "nature"
        
        return self.styles[style](theme)

    def _generate_sonnet(self, theme):
        theme_words = self.themes[theme]
        poem = "\n".join([
            f"Shall I compare thee to a {random.choice(theme_words)}'s day?",
            f"Thou art more lovely and more temperate:",
            "Rough winds do shake the darling buds of May,",
            f"And summer's lease hath all too short a date:",
            # ... remaining lines of a sonnet
        ])
        return poem

    def _generate_haiku(self, theme):
        theme_words = self.themes[theme]
        poem = "\n".join([
            f"An old silent pond...",
            f"A frog jumps into the {random.choice(theme_words)} —",
            "Splash! Silence again."
        ])
        return poem

    def _generate_free_verse(self, theme):
        theme_words = self.themes[theme]
        poem = "\n".join([
            f"In the {random.choice(theme_words)} of night,",
            f"The {random.choice(theme_words)} whispers secrets,",
            "Untold tales of the past and future,",
            f"Echoes of {random.choice(theme_words)},",
            "In the stillness, I find peace."
        ])
        return poem
