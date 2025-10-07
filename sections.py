import random
from pprint import pprint
from typing import List

def _shuffle_join(items: List[str]) -> str:
    """
    Assemble a string from a randomly shuffled copy of a list.

    :param items: A list of HTML fragments that are safe to swap.
    :return: A concatenated string of shuffled elements.
    """

    items_copy = list(items)
    random.shuffle(items_copy)
    return "".join(items_copy)


def hero(cfg):
    """ Hero section

    The <h1> heading is fixed at the top.
    The <p> paragraph and <a> link button are randomly swapped on each build.
    """

    heading = "<h1>Simple Static Site</h1>"

    body_items = [
        '<p>Generated with Python. New look every run.</p>',
        '<a class="btn" href="#contact">Get in touch</a>',
    ]
    body = _shuffle_join(body_items)
    return f"""
    <section class="container hero">
    {heading}
    {body}
    """


def features(cfg):
    """The Features section with cards in a grid.

    The <h2> is static.
    The order of the cards changes randomly, but the card contents remain the same to maintain the meaning.
    """

    heading = '<h2>Features</h2>'

    cards = [
        '<div class="card"><h3>Fast Setup</h3><p>Spin up a site in seconds.</p></div>',
        '<div class="card"><h3>No JS</h3><p>Pure HTML + CSS.</p></div>',
        '<div class="card"><h3>Adaptive</h3><p>Looks good on phone and desktop.</p></div>'
    ]
    cards_html = _shuffle_join(cards)

    return f"""
            <section class="container" id="features">
            {heading}
              <div class="features">
                {cards_html}
              </div>
            </section>
            """

def faq(cfg):
    """
    Generate a FAQ (Frequently Asked Questions) section.

    Args:
        cfg (dict): Theme configuration with colors and fonts.

    Returns:
        str: HTML markup for the FAQ section with randomized order of questions.
    """
    heading = '<h2>FAQ</h2>'
    questions = [
        "<details><summary>What is StaticGen?</summary><p>It’s a small static site generator that builds randomized layouts.</p></details>",
        "<details><summary>Can I customize the theme?</summary><p>Yes, each build uses a random theme and font combination.</p></details>",
        "<details><summary>Does it support mobile?</summary><p>Absolutely. The layout is responsive by default.</p></details>",
        "<details><summary>Can I add my own sections?</summary><p>Sure. Just extend the code in sections.py and hook them in builder.py.</p></details>",
        "<details><summary>Is the output SEO-friendly?</summary><p>Yes. It generates clean, static HTML pages.</p></details>"
    ]
    content = _shuffle_join(questions)

    return f"""
    <section class="faq">
        {heading}
        <div class="container">
            {content}
          </div>
        </section>
    """

def contacts(cfg):
    """
    Contact section with a form.

    <h2> is static.
    Randomly swap the order of the name, email, and textarea fields, but the submit button always appears after the inputs.
    """

    heading = '<h2>Contact</h2>'

    inputs = [
        '<input type="text" name="name" placeholder="Your name" required>',
        '<input type="email" name="email" placeholder="Email" required>',
        '<textarea name="message" rows="4" placeholder="Message"></textarea>',
    ]

    inputs_html = _shuffle_join(inputs)
    return f"""
        <section class="container" id="contact">
          {heading}
          <form>
            {inputs_html}
            <button class="btn" type="submit">Send</button>
          </form>
        </section>
        """


def quotes(cfg):
    """Quotes section. Cards with user quotes are randomly shuffled."""

    heading = '<h2>Quotes</h2>'

    quotes = [
        '<div class="card"><p>"Imagination is more important than knowledge."</p><span>— Albert Einstein</span></div>',
        '<div class="card"><p>"Science is a way of thinking much more than it is a body of knowledge."</p><span>— Carl Sagan</span></div>',
        '<div class="card"><p>"The important thing is to never stop questioning."</p><span>— Albert Einstein</span></div>',
        '<div class="card"><p>"Somewhere, something incredible is waiting to be known."</p><span>— Carl Sagan</span></div>',
        '<div class="card"><p>"Research is what I’m doing when I don’t know what I’m doing."</p><span>— Wernher von Braun</span></div>',
        '<div class="card"><p>"We are what we repeatedly do. Excellence, then, is not an act, but a habit."</p><span>— Aristotle</span></div>',
    ]

    content = _shuffle_join(quotes)
    return f"""
    <section class="container" id="quotes">
        {heading}
        <div class="grid">
            {content}
        </div>
    </section>
    """

def pricing(cfg):
    """Pricing section. Randomly changes the order of plains"""
    heading = '<h2>Pricing</h2>'
    plans = [
        '<div class="card"><h3>Free</h3><p>Basic features</p><p class="price">$0</p></div>',
        '<div class="card highlight"><h3>Pro</h3><p>Full access</p><p class="price">$9</p></div>',
        '<div class="card"><h3>Team</h3><p>Up to 10 users</p><p class="price">$29</p></div>',
    ]
    content = _shuffle_join(plans)
    return f"""
    <section class="container" id="pricing">
        {heading}
        <div class="grid pricing">
            {content}
        </div>
    </section>
    """

def gallery(cfg):
    """Gallery section with placeholder images"""
    heading = '<h2>Gallery</h2>'
    images = [f'<img src="https://picsum.photos/seed/{i}/400/300">' for i in range (1, 9)]
    content = _shuffle_join(images)

    return f"""
    <section class="container" id="gallery">
        {heading}
        <div class="grid gallery">
            {content}
        </div>
    </section>
    """