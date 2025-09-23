def hero(cfg):
    return """
<section class="container hero">
  <h1>Simple Static Site</h1>
  <p>Generated with Python. New look every run.</p>
  <a class="btn" href="#contact">Get in touch</a>
</section>
"""

def features(cfg):
    return """
            <section class="container" id="features">
              <h2>Features</h2>
              <div class="features">
                <div class="card"><h3>Fast Setup</h3><p>Spin up a site in seconds.</p></div>
                <div class="card"><h3>No JS</h3><p>Pure HTML + CSS.</p></div>
                <div class="card"><h3>Adaptive</h3><p>Looks good on phone and desktop.</p></div>
              </div>
            </section>
            """

def contacts(cfg):
    return """
        <section class="container" id="contact">
          <h2>Contact</h2>
          <form>
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" rows="4" placeholder="Message"></textarea>
            <button class="btn" type="submit">Send</button>
          </form>
        </section>
        """
