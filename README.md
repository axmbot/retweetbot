Welcome to the Group Retweet Bot.

This bot has not yet been updated for Twitter API 1.1 but it was working quite nicely until then.

The Group Retweet Bot is designed for a group of Twitter users managing or tweeting from a single Twitter account. It's especially suited for those discussing a niche topic. It copies tweets they make with a specified hashtag and appends their initials.  It's ideal for folks who contribute to a group blog and also want to tweet from the blog's Twitter account.

If you tweet: "Cool new thing about China. #88", and the bot is checking for all tweets with "#88", it will simply tweet "Cool new thing about China ^AXM".  This should even work if you tweet "#88 Cool new thing about China."


This bot has the following features:

* Follows a specific group of people. You just need to set up a dict with the preferred acronym and their Twitter handle.
* Scans for a 'checkvariable', which is the hashtag you're checking for. The bot will only retweet tweets that contain this checkvariable, regardless of where in the tweet the checkvariable appears.
* Sends a direct message to the user if their tweet, when adding their initials, is too long and asks them to shorten the tweet by such and such characters. This mostly won't be a problem if you have short acronyms.
* It's designed to just work, without needing to set up a database. It does this by scanning the latest tweets from the bot, rather than storing converted tweets in a database.
* The database-dependent version has a few more options, including the ability to scan for specific keywords.  To keep things simple, it runs on shelve.
* Limits the number of tweets it sends out each time the script runs. You can set this number as low or high as you need to.

This example is implemented for @88_bartenders, a group account for 88 Bar's bloggers. 88 Bar is a popular blog about Chinese tech and design. Check us out at http://www.88-bar.com!

GNU Affero Public License Statement

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
