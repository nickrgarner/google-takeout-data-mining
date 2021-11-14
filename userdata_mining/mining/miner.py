from userdata_mining.utils import get_username, debug, info
from userdata_mining.mining import parse_fit_data
from userdata_mining.mining import parse_autofill, parse_browser_history
from userdata_mining.mining import parse_maps_data
from userdata_mining.mining import parse_maps
from userdata_mining.mining import parse_hangouts_data
from userdata_mining.mining import parse_mail_data
from userdata_mining.mining import parse_yt_comments, parse_yt_watch_history
from userdata_mining.mining import parse_subscribed_channels, parse_liked_videos
from userdata_mining.mining import parse_chats_data
from userdata_mining.mining import parse_play_data
from userdata_mining.mining import parse_pay_data
from userdata_mining.mining import parse_access_log_data
from userdata_mining.embedding import Embedding
from userdata_mining.mining import parse_insta_ads_viewed
from userdata_mining.mining import parse_insta_music_heard
from userdata_mining.mining import parse_insta_videos_watched
from userdata_mining.mining import parse_insta_ads_interest
from userdata_mining.mining import parse_insta_your_topics
from userdata_mining.mining import parse_insta_your_reels_topics
from userdata_mining.mining import parse_insta_your_reels_sentiments
from userdata_mining.mining import parse_insta_saved_posts
from userdata_mining.mining import parse_insta_account_searches
from userdata_mining.mining import parse_insta_monetization_eligibility
from userdata_mining.mining import parse_insta_liked_comments
from userdata_mining.mining import parse_insta_liked_posts
from userdata_mining.mining import parse_insta_post_comments
from userdata_mining.mining import parse_insta_information_submitted
from userdata_mining.mining import parse_insta_posts_viewed
from userdata_mining.mining import parse_insta_suggested_accounts_viewed
from userdata_mining.mining import parse_insta_account_based_in
from userdata_mining.mining import parse_insta_comments_allowed_from
from userdata_mining.mining import parse_insta_use_cross_app_messaging
from userdata_mining.mining import parse_insta_emoji_sliders
from userdata_mining.mining import parse_insta_polls
from userdata_mining.mining import parse_insta_quizzes
from userdata_mining.mining import parse_insta_archived_posts
from userdata_mining.mining import parse_insta_stories
from userdata_mining.mining import parse_insta_followers
from userdata_mining.mining import parse_insta_following
from userdata_mining.mining import parse_insta_hide_story_from
from userdata_mining.mining import parse_insta_messages

from userdata_mining.mining import parse_fb_advertisers
from userdata_mining.mining import parse_fb_apps_and_websites
from userdata_mining.mining import parse_fb_posts_from_apps_and_websites
from userdata_mining.mining import parse_fb_your_topics
from userdata_mining.mining import parse_fb_comments
from userdata_mining.mining import parse_fb_reactions
from userdata_mining.mining import parse_fb_search_history
from userdata_mining.mining import parse_fb_pages_you_follow
from userdata_mining.mining import parse_fb_pages_you_liked
from userdata_mining.mining import parse_fb_ads_interest
from userdata_mining.mining import parse_fb_friend_peer_group
from userdata_mining.mining import parse_fb_groups_comments
from userdata_mining.mining import parse_fb_groups_membership
from userdata_mining.mining import parse_fb_groups_posts
from userdata_mining.mining import parse_fb_messages
from abc import ABC
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
import pickle
import numpy as np
import pandas as pd


class DataMiner(ABC):
    """
    A base class for data miners. Presents high-level functions that
    can be used by both users and subclasses, which provide more
    detailed functionality.
    """

    def __init__(self, data_path='.', user=None):
        """
        Initializes the data miner.

        :param {str} data_path - Path to the data/ folder.
        :param {str} user - The user name. If None, infers it automatically.
        """
        self.data_path = data_path

        if user is None:
            self.user = get_username(self.data_path)
        else:
            self.user = user

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __repr__(self):
        """
        Returns a string representation of the data stored by
        the object.
        """
        string = ''
        variables = [x for x in dir(self) if not x.startswith(
            '_') and not callable(self[x])]
        for key in variables:
            string += f'{key}: {self[key]}\n'
        return string

    def mine_data(self, data_path='.'):
        return NotImplemented


class FbInstaDataMiner(DataMiner):
    """
    Mines Instagram data.
    """

    def mine_data(self):
        """
        Mines all data of Instagram and Facebook
        
        :return {dict} A dictonary with mined, embedded data
        """
        ads_data = parse_insta_ads_viewed(self.user, data_path=self.data_path)
        music_heard_data = parse_insta_music_heard(self.user, data_path=self.data_path)
        videos_watched_data = parse_insta_videos_watched(self.user, data_path=self.data_path)
        ads_interest_data = parse_insta_ads_interest(self.user, data_path=self.data_path)
        your_topics_data = parse_insta_your_topics(self.user, data_path=self.data_path)
        reels_topics_data = parse_insta_your_reels_topics(self.user, data_path=self.data_path)
        reels_sentiments_data = parse_insta_your_reels_sentiments(self.user, data_path=self.data_path)
        saved_posts_data = parse_insta_saved_posts(self.user, data_path=self.data_path)
        account_searches_data = parse_insta_account_searches(self.user, data_path=self.data_path)
        memo_data = parse_insta_monetization_eligibility(self.user, data_path=self.data_path)
        liked_comments_data = parse_insta_liked_comments(self.user, data_path=self.data_path)
        liked_posts_data = parse_insta_liked_posts(self.user, data_path=self.data_path)
        post_comments_data = parse_insta_post_comments(self.user, data_path=self.data_path)
        info_submitted_data = parse_insta_information_submitted(self.user, data_path=self.data_path)
        posts_viewed_data = parse_insta_posts_viewed(self.user, data_path=self.data_path)
        accounts_viewed_data = parse_insta_suggested_accounts_viewed(self.user, data_path=self.data_path)
        accounts_based_in_data = parse_insta_account_based_in(self.user, data_path=self.data_path)
        comments_data = parse_insta_comments_allowed_from(self.user, data_path=self.data_path)
        cross_app_data = parse_insta_use_cross_app_messaging(self.user, data_path=self.data_path)
        emojis_data = parse_insta_emoji_sliders(self.user, data_path=self.data_path)
        polls_data = parse_insta_polls(self.user, data_path=self.data_path)
        quizzes_data = parse_insta_quizzes(self.user, data_path=self.data_path)
        archived_posts_data = parse_insta_archived_posts(self.user, data_path=self.data_path)
        stories_data = parse_insta_stories(self.user, data_path=self.data_path)
        followers_data = parse_insta_followers(self.user, data_path=self.data_path)
        following_data = parse_insta_following(self.user, data_path=self.data_path)
        hide_story_data = parse_insta_hide_story_from(self.user, data_path=self.data_path)
        messages_data = parse_insta_messages(self.user, data_path=self.data_path)

        info('Data parsed.')

        info('Embedding text data. This may take a while.')
        embedding = Embedding(model='bert-base-uncased')

        if ads_data:
            info('Embedding Instagram Ads data. This may take a while.')
            self.ads_embeddings = [
                embedding.embed(x) for x in ads_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_ads.pickle', 'wb') as f:
                pickle.dump(self.ads_embeddings, f)
        else:
            self.ads_embeddings = []

        if music_heard_data:
            info('Embedding Instagram Music Heard data. This may take a while.')
            self.music_heard_embeddings = [
                embedding.embed(x) for x in music_heard_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_music.pickle', 'wb') as f:
                pickle.dump(self.music_heard_embeddings, f)
        else:
            self.music_heard_embeddings = []

        if videos_watched_data:
            info('Embedding Instagram Videos Watched data. This may take a while.')
            self.videos_watched_embeddings = [
                embedding.embed(x) for x in videos_watched_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_videos.pickle', 'wb') as f:
                pickle.dump(self.videos_watched_embeddings, f)
        else:
            self.videos_watched_embeddings = []

        if ads_interest_data:
            info('Embedding Instagram Ads Interest data. This may take a while.')
            self.ads_interest_embeddings = [
                embedding.embed(x) for x in ads_interest_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_ads_interest.pickle', 'wb') as f:
                pickle.dump(self.ads_interest_embeddings, f)
        else:
            self.ads_interest_embeddings = []

        if your_topics_data:
            info('Embedding Instagram Topics data. This may take a while.')
            self.your_topics_embeddings = [
                embedding.embed(x) for x in your_topics_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_topics.pickle', 'wb') as f:
                pickle.dump(self.your_topics_embeddings, f)
        else:
            self.your_topics_embeddings = []

        if reels_topics_data:
            info('Embedding Instagram Reels data. This may take a while.')
            self.reels_topics_embeddings = [
                embedding.embed(x) for x in reels_topics_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_reels_topics.pickle', 'wb') as f:
                pickle.dump(self.reels_topics_embeddings, f)
        else:
            self.reels_topics_embeddings = []

        if reels_sentiments_data:
            info('Embedding Instagram Reels Sentiments data. This may take a while.')
            self.reels_sentiments_embeddings = [
                embedding.embed(x) for x in reels_sentiments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_reels_sentiments.pickle', 'wb') as f:
                pickle.dump(self.reels_sentiments_embeddings, f)
        else:
            self.reels_sentiments_embeddings = []

        if saved_posts_data:
            info('Embedding Instagram Saved Posts data. This may take a while.')
            self.saved_posts_embeddings = [
                embedding.embed(x) for x in saved_posts_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_saved_posts.pickle', 'wb') as f:
                pickle.dump(self.saved_posts_embeddings, f)
        else:
            self.saved_posts_embeddings = []

        if account_searches_data:
            info('Embedding Instagram Account Searches data. This may take a while.')
            self.account_searches_embeddings = [
                embedding.embed(x) for x in account_searches_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_account_searches.pickle', 'wb') as f:
                pickle.dump(self.account_searches_embeddings, f)
        else:
            self.account_searches_embeddings = []

        if memo_data:
            info('Embedding Instagram Memo data. This may take a while.')
            self.memo_embeddings = [
                embedding.embed(x) for x in memo_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_memo_data.pickle', 'wb') as f:
                pickle.dump(self.memo_embeddings, f)
        else:
            self.memo_embeddings = []

        if liked_comments_data:
            info('Embedding Instagram Liked Comments data. This may take a while.')
            self.liked_comments_embeddings = [
                embedding.embed(x) for x in liked_comments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_liked_comments.pickle', 'wb') as f:
                pickle.dump(self.liked_comments_embeddings, f)
        else:
            self.liked_comments_embeddings = []

        if liked_posts_data:
            info('Embedding Instagram Liked Posts data. This may take a while.')
            self.liked_posts_embeddings = [
                embedding.embed(x) for x in liked_posts_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_liked_posts.pickle', 'wb') as f:
                pickle.dump(self.liked_posts_embeddings, f)
        else:
            self.liked_posts_embeddings = []

        if post_comments_data:
            info('Embedding Instagram Post Comments data. This may take a while.')
            self.post_comments_embeddings = [
                embedding.embed(x) for x in post_comments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_post_comments.pickle', 'wb') as f:
                pickle.dump(self.post_comments_embeddings, f)
        else:
            self.post_comments_embeddings = []

        if info_submitted_data:
            info('Embedding Instagram Info Submitted data. This may take a while.')
            self.info_submitted_embeddings = [
                embedding.embed(x) for x in info_submitted_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_info_submitted.pickle', 'wb') as f:
                pickle.dump(self.info_submitted_embeddings, f)
        else:
            self.info_submitted_embeddings = []

        if posts_viewed_data:
            info('Embedding Instagram Posts Viewed data. This may take a while.')
            self.posts_viewed_embeddings = [
                embedding.embed(x) for x in posts_viewed_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_posts_viewed.pickle', 'wb') as f:
                pickle.dump(self.posts_viewed_embeddings, f)
        else:
            self.posts_viewed_embeddings = []

        if accounts_viewed_data:
            info('Embedding Instagram Accounts Viewed data. This may take a while.')
            self.accounts_viewed_embeddings = [
                embedding.embed(x) for x in accounts_viewed_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_accounts_viewed.pickle', 'wb') as f:
                pickle.dump(self.accounts_viewed_embeddings, f)
        else:
            self.accounts_viewed_embeddings = []

        if accounts_based_in_data:
            info('Embedding Instagram Accounts Based in data. This may take a while.')
            self.accounts_based_in_embeddings = [
                embedding.embed(x) for x in accounts_based_in_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_accounts_based.pickle', 'wb') as f:
                pickle.dump(self.accounts_based_in_embeddings, f)
        else:
            self.accounts_based_in_embeddings = []

        if comments_data:
            info('Embedding Instagram Comments data. This may take a while.')
            self.comments_embeddings = [
                embedding.embed(x) for x in comments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_comments_data.pickle', 'wb') as f:
                pickle.dump(self.comments_embeddings, f)
        else:
            self.comments_embeddings = []

        if cross_app_data:
            info('Embedding Instagram Cross App data. This may take a while.')
            self.cross_app_embeddings = [
                embedding.embed(x) for x in cross_app_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_cross_app.pickle', 'wb') as f:
                pickle.dump(self.cross_app_embeddings, f)
        else:
            self.cross_app_embeddings = []

        if emojis_data:
            info('Embedding Instagram Emojis data. This may take a while.')
            self.emojis_embeddings = [
                embedding.embed(x) for x in emojis_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_emojis.pickle', 'wb') as f:
                pickle.dump(self.emojis_embeddings, f)
        else:
            self.emojis_embeddings = []

        if polls_data:
            info('Embedding Instagram Polls data. This may take a while.')
            self.polls_embeddings = [
                embedding.embed(x) for x in polls_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_polls.pickle', 'wb') as f:
                pickle.dump(self.polls_embeddings, f)
        else:
            self.polls_embeddings = []

        if quizzes_data:
            info('Embedding Instagram Quizzes data. This may take a while.')
            self.quizzes_embeddings = [
                embedding.embed(x) for x in quizzes_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_quizzes.pickle', 'wb') as f:
                pickle.dump(self.quizzes_embeddings, f)
        else:
            self.quizzes_embeddings = []

        if archived_posts_data:
            info('Embedding Instagram Archived Posts data. This may take a while.')
            self.archived_posts_embeddings = [
                embedding.embed(x) for x in archived_posts_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_archived_posts.pickle', 'wb') as f:
                pickle.dump(self.archived_posts_embeddings, f)
        else:
            self.archived_posts_embeddings = []

        if stories_data:
            info('Embedding Instagram Stories data. This may take a while.')
            self.stories_embeddings = [
                embedding.embed(x) for x in stories_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_stories.pickle', 'wb') as f:
                pickle.dump(self.stories_embeddings, f)
        else:
            self.stories_embeddings = []

        if followers_data:
            info('Embedding Instagram Followers data. This may take a while.')
            self.followers_embeddings = [
                embedding.embed(x) for x in followers_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_followers.pickle', 'wb') as f:
                pickle.dump(self.followers_embeddings, f)
        else:
            self.followers_embeddings = []

        if following_data:
            info('Embedding Instagram Following data. This may take a while.')
            self.following_embeddings = [
                embedding.embed(x) for x in following_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_following.pickle', 'wb') as f:
                pickle.dump(self.following_embeddings, f)
        else:
            self.following_embeddings = []

        if hide_story_data:
            info('Embedding Instagram Hide Story data. This may take a while.')
            self.hide_story_embeddings = [
                embedding.embed(x) for x in hide_story_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_hide_story.pickle', 'wb') as f:
                pickle.dump(self.hide_story_embeddings, f)
        else:
            self.hide_story_embeddings = []

        if messages_data:
            info('Embedding Instagram Messages data. This may take a while.')
            self.messages_embeddings = [
                embedding.embed(x) for x in messages_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_messgaes.pickle', 'wb') as f:
                pickle.dump(self.messages_embeddings, f)
        else:
            self.messages_embeddings = []

        if ads_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_ads.pickle', 'wb') as f:
                self.ads_embeddings = pickle.load(f)

        if music_heard_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_music.pickle', 'wb') as f:
                self.music_heard_embeddings = pickle.load(f)

        if videos_watched_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_videos.pickle', 'wb') as f:
                self.videos_watched_embeddings = pickle.load(f)

        if ads_interest_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_ads_interest.pickle', 'wb') as f:
                self.ads_interest_embeddings = pickle.load(f)

        if your_topics_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_topics.pickle', 'wb') as f:
                self.your_topics_embeddings = pickle.load(f)

        if reels_topics_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_reels_topics.pickle', 'wb') as f:
                self.reels_topics_embeddings = pickle.load(f)

        if reels_sentiments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_reels_sentiments.pickle', 'wb') as f:
                self.reels_sentiments_embeddings = pickle.load(f)

        if saved_posts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_saved_posts.pickle', 'wb') as f:
                self.saved_posts_embeddings = pickle.load(f)

        if account_searches_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_account_searches.pickle', 'wb') as f:
                self.account_searches_embeddings = pickle.load(f)

        if memo_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_memo_data.pickle', 'wb') as f:
                self.memo_embeddings = pickle.load(f)

        if liked_comments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_liked_comments.pickle', 'wb') as f:
                self.liked_comments_embeddings = pickle.load(f)

        if liked_posts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_liked_posts.pickle', 'wb') as f:
                self.liked_posts_embeddings = pickle.load(f)

        if post_comments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_post_comments.pickle', 'wb') as f:
                self.post_comments_embeddings = pickle.load(f)

        if info_submitted_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_info_submitted.pickle', 'wb') as f:
                self.info_submitted_embeddings = pickle.load(f)

        if posts_viewed_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_posts_viewed.pickle', 'wb') as f:
                self.posts_viewed_embeddings = pickle.load(f)

        if accounts_viewed_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_accounts_viewed.pickle', 'wb') as f:
                self.accounts_viewed_embeddings = pickle.load(f)

        if accounts_based_in_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_accounts_based.pickle', 'wb') as f:
                self.accounts_based_in_embeddings = pickle.load(f)

        if comments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_comments_data.pickle', 'wb') as f:
                self.comments_embeddings = pickle.load(f)

        if cross_app_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_cross_app.pickle', 'wb') as f:
                self.cross_app_embeddings = pickle.load(f)

        if emojis_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_emojis.pickle', 'wb') as f:
                self.emojis_embeddings = pickle.load(f)

        if polls_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_polls.pickle', 'wb') as f:
                self.polls_embeddings = pickle.load(f)

        if quizzes_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_quizzes.pickle', 'wb') as f:
                self.quizzes_embeddings = pickle.load(f)

        if archived_posts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_archived_posts.pickle', 'wb') as f:
                self.archived_posts_embeddings = pickle.load(f)

        if stories_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_stories.pickle', 'wb') as f:
                self.stories_embeddings = pickle.load(f)

        if followers_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_followers.pickle', 'wb') as f:
                self.followers_embeddings = pickle.load(f)

        if following_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_following.pickle', 'wb') as f:
                self.following_embeddings = pickle.load(f)

        if hide_story_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_hide_story.pickle', 'wb') as f:
                self.hide_story_embeddings = pickle.load(f)

        if messages_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/insta_messgaes.pickle', 'wb') as f:
                self.messages_embeddings = pickle.load(f)

        fb_ads_data = parse_fb_advertisers(self.user, data_path=self.data_path)
        fb_apps_data = parse_fb_apps_and_websites(self.user, data_path=self.data_path)
        fb_posts_apps_data = parse_fb_posts_from_apps_and_websites(self.user, data_path=self.data_path)
        fb_your_topics_data = parse_fb_your_topics(self.user, data_path=self.data_path)
        fb_comments_data = parse_fb_comments(self.user, data_path=self.data_path)
        fb_reactions_data = parse_fb_reactions(self.user, data_path=self.data_path)
        fb_search_historydata = parse_fb_search_history(self.user, data_path=self.data_path)
        fb_saved_posts_data = parse_fb_pages_you_follow(self.user, data_path=self.data_path)
        fb_pages_you_follow_data = parse_fb_pages_you_liked(self.user, data_path=self.data_path)
        fb_ads_interest_data = parse_fb_ads_interest(self.user, data_path=self.data_path)
        fb_friend_peer_group_data = parse_fb_friend_peer_group(self.user, data_path=self.data_path)
        fb_groups_comments_data = parse_fb_groups_comments(self.user, data_path=self.data_path)
        fb_groups_membership_data = parse_fb_groups_membership(self.user, data_path=self.data_path)
        fb_groups_posts_data = parse_fb_groups_posts(self.user, data_path=self.data_path)
        fb_messages_data = parse_fb_messages(self.user, data_path=self.data_path)

        if fb_ads_data:
            info('Embedding FB Ads data. This may take a while.')
            self.fb_ads_embeddings = [
                embedding.embed(x) for x in fb_ads_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_ads.pickle', 'wb') as f:
                pickle.dump(self.fb_ads_embeddings, f)
        else:
            self.fb_ads_embeddings = []

        if fb_apps_data:
            info('Embedding FB Apps data. This may take a while.')
            self.fb_apps_embeddings = [
                embedding.embed(x) for x in fb_apps_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_apps.pickle', 'wb') as f:
                pickle.dump(self.fb_apps_embeddings, f)
        else:
            self.fb_apps_embeddings = []

        if fb_posts_apps_data:
            info('Embedding FB Posts apps data. This may take a while.')
            self.fb_posts_apps_embeddings = [
                embedding.embed(x) for x in fb_posts_apps_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_posts_apps.pickle', 'wb') as f:
                pickle.dump(self.fb_posts_apps_embeddings, f)
        else:
            self.fb_posts_apps_embeddings = []

        if fb_your_topics_data:
            info('Embedding FB Topics data. This may take a while.')
            self.fb_your_topics_embeddings = [
                embedding.embed(x) for x in fb_your_topics_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_topics.pickle', 'wb') as f:
                pickle.dump(self.fb_your_topics_embeddings, f)
        else:
            self.fb_your_topics_embeddings = []

        if fb_comments_data:
            info('Embedding FB Comments data. This may take a while.')
            self.fb_comments_embeddings = [
                embedding.embed(x) for x in fb_comments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_comments.pickle', 'wb') as f:
                pickle.dump(self.fb_comments_embeddings, f)
        else:
            self.fb_comments_embeddings = []

        if fb_reactions_data:
            info('Embedding FB Reactions data. This may take a while.')
            self.fb_reactions_embeddings = [
                embedding.embed(x) for x in fb_reactions_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_reactions.pickle', 'wb') as f:
                pickle.dump(self.fb_reactions_embeddings, f)
        else:
            self.fb_reactions_embeddings = []

        if fb_search_historydata:
            info('Embedding FB Search History data. This may take a while.')
            self.fb_search_history_embeddings = [
                embedding.embed(x) for x in fb_search_historydata]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_search_history.pickle', 'wb') as f:
                pickle.dump(self.fb_search_history_embeddings, f)
        else:
            self.fb_search_history_embeddings = []

        if fb_saved_posts_data:
            info('Embedding FB Saved Posts data. This may take a while.')
            self.fb_saved_posts_embeddings = [
                embedding.embed(x) for x in fb_saved_posts_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_saved_posts.pickle', 'wb') as f:
                pickle.dump(self.fb_saved_posts_embeddings, f)
        else:
            self.fb_saved_posts_embeddings = []

        if fb_pages_you_follow_data:
            info('Embedding FB Pages You Follow data. This may take a while.')
            self.fb_pages_you_follow_embeddings = [
                embedding.embed(x) for x in fb_pages_you_follow_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_pages_you_follow.pickle', 'wb') as f:
                pickle.dump(self.fb_pages_you_follow_embeddings, f)
        else:
            self.fb_pages_you_follow_embeddings = []

        if fb_ads_interest_data:
            info('Embedding FB Ads Interest data. This may take a while.')
            self.fb_ads_interest_embeddings = [
                embedding.embed(x) for x in fb_ads_interest_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_ads_interest.pickle', 'wb') as f:
                pickle.dump(self.fb_ads_interest_embeddings, f)
        else:
            self.fb_ads_interest_embeddings = []

        if fb_friend_peer_group_data:
            info('Embedding FB Friend Peer group data. This may take a while.')
            self.fb_friend_peer_group_embeddings = [
                embedding.embed(x) for x in fb_friend_peer_group_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_friend_peer_group.pickle', 'wb') as f:
                pickle.dump(self.fb_friend_peer_group_embeddings, f)
        else:
            self.fb_friend_peer_group_embeddings = []

        if fb_groups_comments_data:
            info('Embedding FB groups comments data. This may take a while.')
            self.fb_groups_comments_embeddings = [
                embedding.embed(x) for x in fb_groups_comments_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_comments.pickle', 'wb') as f:
                pickle.dump(self.fb_groups_comments_embeddings, f)
        else:
            self.fb_groups_comments_embeddings = []

        if fb_groups_membership_data:
            info('Embedding FB groups membership data. This may take a while.')
            self.fb_groups_membership_embeddings = [
                embedding.embed(x) for x in fb_groups_membership_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_membership.pickle', 'wb') as f:
                pickle.dump(self.fb_groups_membership_embeddings, f)
        else:
            self.fb_groups_membership_embeddings = []

        if fb_groups_posts_data:
            info('Embedding FB groups posts data. This may take a while.')
            self.fb_groups_posts_embeddings = [
                embedding.embed(x) for x in fb_groups_posts_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_posts.pickle', 'wb') as f:
                pickle.dump(self.fb_groups_posts_embeddings, f)
        else:
            self.fb_groups_posts_embeddings = []

        if fb_messages_data:
            info('Embedding FB Messages data. This may take a while.')
            self.fb_messages_embeddings = [
                embedding.embed(x) for x in fb_messages_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_messages.pickle', 'wb') as f:
                pickle.dump(self.fb_messages_embeddings, f)
        else:
            self.fb_messages_embeddings = []

        if fb_ads_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_ads.pickle', 'wb') as f:
                self.fb_ads_embeddings = pickle.load(f)

        if fb_apps_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_apps.pickle', 'wb') as f:
                self.fb_ads_interest_embeddings = pickle.load(f)

        if fb_posts_apps_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_posts_apps.pickle', 'wb') as f:
                self.fb_posts_apps_embeddings = pickle.load(f)

        if fb_your_topics_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_topics.pickle', 'wb') as f:
                self.fb_your_topics_embeddings = pickle.load(f)

        if fb_comments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_comments.pickle', 'wb') as f:
                self.fb_comments_embeddings = pickle.load(f)

        if fb_reactions_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_reactions.pickle', 'wb') as f:
                self.fb_reactions_embeddings = pickle.load(f)

        if fb_search_historydata is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_search_history.pickle', 'wb') as f:
                self.fb_search_history_embeddings = pickle.load(f)

        if fb_saved_posts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_saved_posts.pickle', 'wb') as f:
                self.fb_saved_posts_embeddings = pickle.load(f)

        if fb_pages_you_follow_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_pages_you_follow.pickle', 'wb') as f:
                self.fb_pages_you_follow_embeddings = pickle.load(f)

        if fb_ads_interest_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_ads_interest.pickle', 'wb') as f:
                self.fb_ads_interest_embeddings = pickle.load(f)

        if fb_friend_peer_group_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_friend_peer_group.pickle', 'wb') as f:
                self.fb_friend_peer_group_embeddings = pickle.load(f)

        if fb_groups_comments_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_comments.pickle', 'wb') as f:
                self.fb_groups_comments_embeddings = pickle.load(f)

        if fb_groups_membership_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_membership.pickle', 'wb') as f:
                self.fb_groups_membership_embeddings = pickle.load(f)

        if fb_groups_posts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_groups_posts.pickle', 'wb') as f:
                self.fb_groups_posts_embeddings = pickle.load(f)

        if fb_messages_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/fb_messages.pickle', 'wb') as f:
                self.fb_messages_embeddings = pickle.load(f)

        info(f'Embedding complete. Data details:\n' +
             f'Insta Advertisements Data: {len(self.ads_embeddings)} item(s).\n' +
             f'Insta Music heard: {len(self.music_heard_embeddings)} item(s).\n' +
             f'Insta Videos watched: {len(self.videos_watched_embeddings)} item(s).\n' +
             f'Insta Interests: {len(self.ads_interest_embeddings)} item(s).\n' +
             f'Insta Topics: {len(self.your_topics_embeddings)} item(s).\n' +
             f'Insta Reels Topics: {len(self.reels_topics_embeddings)} item(s).\n' +
             f'Insta Posts Saved: {len(self.reels_sentiments_embeddings)} item(s).\n' +
             f'Insta Account Searches: {len(self.account_searches_embeddings)} item(s).\n' +
             f'Insta Memo Data: {len(self.memo_embeddings)} item(s).\n' +
             f'Insta Liked Comments: {len(self.liked_comments_embeddings)} item(s).\n' +
             f'Insta Liked Posts: {len(self.liked_posts_embeddings)} item(s). \n' +
             f'Insta Post Comments: {len(self.post_comments_embeddings)} item(s).\n' +
             f'Insta Information Submitted: {len(self.info_submitted_embeddings)} item(s).\n' +
             f'Insta Posts viewed: {len(self.posts_viewed_embeddings)} item(s).\n' +
             f'Insta Accounts Viewed: {len(self.accounts_viewed_embeddings)} item(s).\n' +
             f'Insta Accounts based: {len(self.accounts_based_in_embeddings)} item(s).\n' +
             f'Insta Comments: {len(self.comments_embeddings)} item(s).\n' +
             f'Insta Cross App Data: {len(self.cross_app_embeddings)} item(s).\n' +
             f'Insta Emojis: {len(self.emojis_embeddings)} item(s).\n' +
             f'Insta Polls: {len(self.polls_embeddings)} item(s).\n' +
             f'Insta Quizzes: {len(self.quizzes_embeddings)} item(s).\n' +
             f'Insta Archived Posts: {len(self.archived_posts_embeddings)} item(s).\n' +
             f'Insta Stories: {len(self.stories_embeddings)} item(s). \n' +
             f'Insta Followers: {len(self.followers_embeddings)} item(s).\n' +
             f'Insta Following: {len(self.following_embeddings)} item(s).\n' +
             f'Insta Hided story: {len(self.hide_story_embeddings)} item(s).\n' +
             f'Insta Messages: {len(self.messages_embeddings)} item(s).\n' +
             f'FB Advertisements: {len(self.fb_ads_embeddings)} item(s).\n' +
             f'FB Apps: {len(self.fb_apps_embeddings)} item(s).\n' +
             f'FB Posts Apps: {len(self.fb_posts_apps_embeddings)} item(s).\n' +
             f'FB Topics: {len(self.fb_your_topics_embeddings)} item(s).\n' +
             f'FB Comments: {len(self.fb_comments_embeddings)} item(s).\n' +
             f'FB Reactions: {len(self.fb_reactions_embeddings)} item(s).\n' +
             f'FB Search History: {len(self.fb_search_history_embeddings)} item(s).\n' +
             f'FB Saved posts: {len(self.fb_saved_posts_embeddings)} item(s).\n' +
             f'FB Pages followed: {len(self.fb_pages_you_follow_embeddings)} item(s).\n' +
             f'FB Ad interests: {len(self.fb_ads_interest_embeddings)} item(s).\n' +
             f'FB Friend peer group: {len(self.fb_friend_peer_group_embeddings)} item(s). \n' +
             f'FB Group comments: {len(self.fb_groups_comments_embeddings)} item(s).\n' +
             f'FB Group membership: {len(self.fb_groups_membership_embeddings)} item(s).\n' +
             f'FB Group posts: {len(self.fb_groups_posts_embeddings)} item(s).\n' +
             f'FB Messages: {len(self.fb_messages_embeddings)} item(s).')

        return {
            'Insta Advertisements Data': self.ads_embeddings,
            'Insta Music heard': self.music_heard_embeddings,
            'Insta Videos watched': self.videos_watched_embeddings,
            'Insta Interests': self.ads_interest_embeddings,
            'Insta Topics': self.your_topics_embeddings,
            'Insta Reels Topics': self.reels_topics_embeddings,
            'Insta Reels Sentiments': self.reels_sentiments_embeddings,
            'Insta Posts Saved': self.saved_posts_embeddings,
            'Insta Account Searches': self.account_searches_embeddings,
            'Insta Memo Data': self.memo_embeddings,
            'Insta Liked Comments': self.liked_comments_embeddings,
            'Insta Liked Posts': self.liked_posts_embeddings,
            'Insta Post Comments': self.post_comments_embeddings,
            'Insta Information Submitted': self.info_submitted_embeddings,
            'Insta Posts viewed': self.posts_viewed_embeddings,
            'Insta Accounts Viewed': self.accounts_viewed_embeddings,
            'Insta Accounts based': self.accounts_based_in_embeddings,
            'Insta Comments': self.comments_embeddings,
            'Insta Cross App Data': self.cross_app_embeddings,
            'Insta Emojis': self.emojis_embeddings,
            'Insta Polls': self.polls_embeddings,
            'Insta Quizzes': self.quizzes_embeddings,
            'Insta Archived Posts': self.archived_posts_embeddings,
            'Insta Stories': self.stories_embeddings,
            'Insta Followers': self.followers_embeddings,
            'Insta Following': self.following_embeddings,
            'Insta Hided story': self.hide_story_embeddings,
            'Insta Messages': self.messages_embeddings,
            'FB Advertisements': self.fb_ads_embeddings,
            'FB Apps': self.fb_apps_embeddings,
            'FB Posts Apps': self.fb_posts_apps_embeddings,
            'FB Topics': self.fb_your_topics_embeddings,
            'FB Comments': self.fb_comments_embeddings,
            'FB Reactions': self.fb_reactions_embeddings,
            'FB Search History': self.fb_search_history_embeddings,
            'FB Saved posts': self.fb_saved_posts_embeddings,
            'FB Pages followed': self.fb_pages_you_follow_embeddings,
            'FB Ad interests': self.fb_ads_interest_embeddings,
            'FB Friend peer group': self.fb_friend_peer_group_embeddings,
            'FB Group comments': self.fb_groups_comments_embeddings,
            'FB Group membership': self.fb_groups_membership_embeddings,
            'FB Group posts': self.fb_groups_posts_embeddings,
            'FB Messages': self.fb_messages_embeddings
        }


class GoogleDataMiner(DataMiner):
    """
    Mines Google data.
    """

    def mine_data(self):
        """
        Mines all data.

        :return {dict} A dictionary with mined, embedded data
        """
        fit_data = parse_fit_data(self.user, data_path=self.data_path)
        maps_data = parse_maps_data(self.user, data_path=self.data_path)
        autofill_data = parse_autofill(self.user, data_path=self.data_path)
        browser_data = parse_browser_history(
            self.user, data_path=self.data_path)
        hangouts_data = parse_hangouts_data(
            self.user, data_path=self.data_path)
        mail_data = parse_mail_data(self.user, data_path=self.data_path)
        maps_places_data = parse_maps(self.user, self.data_path)
        yt_comments_data = parse_yt_comments(self.user, self.data_path)
        yt_history_data = parse_yt_watch_history(self.user, self.data_path)
        yt_subscribed_data = parse_subscribed_channels(
            self.user, self.data_path)
        yt_liked_data = parse_liked_videos(self.user, self.data_path)
        chats_data = parse_chats_data(self.user, self.data_path)
        movies_data = parse_play_data(self.user, 'movies', self.data_path)
        apps_data = parse_play_data(self.user, 'apps', self.data_path)
        transactions_data = parse_pay_data(self.user, self.data_path)
        activities_data = parse_access_log_data(self.user, self.data_path)

        info('Data parsed.')

        # Extract features from Fit data
        # First, get total distance, total distance in past year,
        # total calories, total calories in past year.
        today = datetime.today()

        if fit_data:
            total_distance = sum([x['distance'] for x in fit_data])
            total_calories = sum([x['calories'] for x in fit_data])
            total_dist_year = sum([x['distance'] for x in fit_data if parser.parse(
                max(x['dates'])).replace(tzinfo=None) < today - relativedelta(years=1)])
            total_cal_year = sum([x['calories'] for x in fit_data if parser.parse(
                max(x['dates'])).replace(tzinfo=None) < today - relativedelta(years=1)])
        else:
            total_distance = 0
            total_calories = 0
            total_dist_year = 0
            total_cal_year = 0

        self.mined_fit_data = {
            'total_dist': total_distance,

            'total_cal': total_calories,
            'total_dist_yr': total_dist_year,
            'total_cal_yr': total_cal_year
        }

        info('Embedding text data. This may take a while.')
        embedding = Embedding(model='bert-base-uncased')

        if activities_data:
            self.activities_embeddings = [
                embedding.embed(x) for x in activities_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/activities.pickle', 'wb') as f:
                pickle.dump(self.activities_embeddings, f)
        else:
            self.activities_embeddings = []

        if apps_data:
            info('Embedding Google Play Apps data. This may take a while.')
            self.apps_embeddings = [
                embedding.embed(x) for x in apps_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/apps.pickle', 'wb') as f:
                pickle.dump(self.apps_embeddings, f)
        else:
            self.apps_embeddings = []

        if autofill_data:
            self.autofill_place_embeddings = [
                embedding.embed(x) for x in autofill_data]
        else:
            self.autofill_place_embeddings = []

        if browser_data:
            self.history_embeddings = [
                embedding.embed(x) for x in browser_data]
        else:
            self.history_embeddings = []

        if hangouts_data:
            info('Embedding Hangouts data. This may take a while.')
            self.messages_embeddings = [
                embedding.embed(x) for x in hangouts_data]
            self.messages_embeddings = [
                x for x in self.messages_embeddings if x is not None]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/hangouts.pickle', 'wb') as f:
                pickle.dump(self.messages_embeddings, f)
        else:
            self.messages_embeddings = []

        if chats_data:
            info('Embedding Google Chat data. This may take a while.')
            self.chats_embeddings = [
                embedding.embed(x) for x in chats_data]
        else:
            self.chats_embeddings = []

        if mail_data:
            info('Embedding email data. This may take a while.')
            self.email_embeddings = [embedding.embed(x) for x in mail_data]
            self.email_embeddings = [
                x for x in self.email_embeddings if x is not None]

            # Cache email embeddings
            with open(f'{self.data_path}/saved/embeddings/mail.pickle', 'wb') as f:
                pickle.dump(self.email_embeddings, f)
        else:
            self.email_embeddings = []

        if movies_data:
            info('Embedding Google Play Movies data. This may take a while.')
            self.movies_embeddings = [
                embedding.embed(x) for x in movies_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/movies.pickle', 'wb') as f:
                pickle.dump(self.movies_embeddings, f)
        else:
            self.movies_embeddings = []

        if transactions_data:
            info('Embedding Google Pay transaction data. This may take a while.')
            self.transactions_embeddings = [
                embedding.embed(x) for x in transactions_data]

            # Cache embeddings
            with open(f'{self.data_path}/saved/embeddings/pay.pickle', 'wb') as f:
                pickle.dump(self.transactions_embeddings, f)
        else:
            self.transactions_embeddings = []

        self.distance_traveled = maps_data['total_distance']
        self.nearby_places_embeddings = [
            embedding.embed(x) for x in maps_data['places']]
        self.maps_places_embeddings = [
            embedding.embed(x) for x in maps_places_data
        ]
        self.yt_comments_embeddings = [
            embedding.embed(x) for x in yt_comments_data
        ]
        self.yt_history_embeddings = [
            embedding.embed(x) for x in yt_history_data
        ]
        self.yt_subscribed_embeddings = [
            embedding.embed(x) for x in yt_subscribed_data
        ]
        self.yt_liked_embeddings = [
            embedding.embed(x) for x in yt_liked_data
        ]

        # Join nearby places with data from Maps (your places)
        self.nearby_places_embeddings = np.vstack(
            (self.nearby_places_embeddings, self.maps_places_embeddings))

        if activities_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/activities.pickle', 'rb') as f:
                self.activities_embeddings = pickle.load(f)

        if apps_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/apps.pickle', 'rb') as f:
                self.apps_embeddings = pickle.load(f)

        if chats_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/chat.pkl', 'rb') as f:
                self.chats_embeddings = pickle.load(f)

        if hangouts_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/hangouts.pickle', 'rb') as f:
                self.messages_embeddings = pickle.load(f)

        if mail_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/mail.pickle', 'rb') as f:
                self.email_embeddings = pickle.load(f)

        if movies_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/movies.pickle', 'rb') as f:
                self.movies_embeddings = pickle.load(f)

        if transactions_data is None:
            # Load cached embeddings
            with open(f'{self.data_path}/saved/embeddings/pay.pickle', 'rb') as f:
                self.transactions_embeddings = pickle.load(f)

        info(f'Embedding complete. Data details:\n' +
             f'Activities: {len(self.activities_embeddings)} item(s).\n' +
             f'Apps: {len(self.apps_embeddings)} item(s).\n' +
             f'Autofill: {len(self.autofill_place_embeddings)} item(s).\n' +
             f'Browser history: {len(self.history_embeddings)} item(s).\n' +
             f'Hangouts: {len(self.messages_embeddings)} item(s).\n' +
             f'Google Chat: {len(self.chats_embeddings)} item(s).\n' +
             f'Google Pay Transactions: {len(self.transactions_embeddings)} item(s).\n' +
             f'Monthly travel estimate: {self.distance_traveled} km.\n' +
             f'Nearby places: {len(self.nearby_places_embeddings)} item(s).\n' +
             f'Email: {len(self.email_embeddings)} item(s).\n' +
             f'Movies: {len(self.movies_embeddings)} item(s). \n' +
             f'YouTube comments: {len(self.yt_comments_embeddings)} item(s).\n' +
             f'YouTube subscriptions: {len(self.yt_subscribed_embeddings)} item(s).\n' +
             f'YouTube liked videos: {len(self.yt_liked_embeddings)} item(s).\n' +
             f'YouTube watch history: {len(self.yt_history_embeddings)} item(s).')

        return {
            'Activities': self.activities_embeddings,
            'Apps': self.apps_embeddings,
            'Autofill': self.autofill_place_embeddings,
            'Browser History': self.history_embeddings,
            'Chat': self.chats_embeddings,
            'Hangouts': self.messages_embeddings,
            'Travel': self.distance_traveled,
            'Nearby Places': self.nearby_places_embeddings,
            'Email': self.email_embeddings,
            'Movies': self.movies_embeddings,
            'Pay Transactions': self.transactions_embeddings,
            'YouTube comments': self.yt_comments_embeddings,
            'YouTube subscriptions': self.yt_subscribed_embeddings,
            'YouTube liked videos': self.yt_liked_embeddings,
            'YouTube watch history': self.yt_history_embeddings
        }
