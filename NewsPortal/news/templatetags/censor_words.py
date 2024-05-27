from django import template

from NewsPortal.NewsPortal.settings import BAN_WORDS

register = (template.Library())

@register.filter()
def censor(text, title_post):
    text_words = set(text.Post.split())
    title_post_words = set(title_post.Post.split())
    filtered_text = text
    filtered_title_post = title_post
    for word in text_words:
        if word.lower() in BAN_WORDS:
            filtered_text = filtered_text.replace(word, word[1:] + "*" * len(word))

    for word in title_post_words:
        if word.lower() in BAN_WORDS:
            filtered_title_post = filtered_title_post.replace(word, word[1:] + "*" * len(word))
    return filtered_text, filtered_title_post





