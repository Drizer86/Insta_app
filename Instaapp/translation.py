from .models import Post, Follow, Comment
from modeltranslation.translator import TranslationOptions,register

@register(Follow)
class FollowTranslationOptions(TranslationOptions):
    fields = ('follower',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('user','description')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('user', 'text')