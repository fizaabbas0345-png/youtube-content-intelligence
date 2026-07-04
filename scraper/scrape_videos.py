import os
import pandas as pd
import yt_dlp

from config import CHANNELS, OUTPUT_FILE


def scrape_channel(channel_url):

    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "playlistend": 30
    }

    rows = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(channel_url + "/videos", download=False)

        channel_name = info.get("title")

        for video in info["entries"]:

            rows.append({

                "channel": channel_name,
                "video_id": video.get("id"),
                "title": video.get("title"),
                "url": f"https://www.youtube.com/watch?v={video.get('id')}"

            })

    return rows

def get_video_details(video_url):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)

    return {
        "views": info.get("view_count"),
        "upload_date": info.get("upload_date"),
        "duration_seconds": info.get("duration"),
        "description": info.get("description"),
        "thumbnail": info.get("thumbnail"),
        "like_count": info.get("like_count"),
        "comment_count": info.get("comment_count"),
        "channel_subscribers": info.get("channel_follower_count"),
        "tags": ", ".join(info.get("tags", []))
    }

def scrape_all():

    all_rows = []

    for index, channel in enumerate(CHANNELS, start=1):

        print("\n" + "=" * 70)
        print(f"Channel {index}/{len(CHANNELS)}")
        print(f"Scraping: {channel}")

        try:
            data = scrape_channel(channel)

        except Exception as e:
            print(f"❌ Failed to scrape channel: {channel}")
            print(e)
            continue

        for video_index, row in enumerate(data, start=1):

            print(f"   [{video_index}/{len(data)}] {row['title']}")

            try:
                details = get_video_details(row["url"])
                row.update(details)

            except Exception as e:

                print(f"Error processing video: {e}")

                row.update({
                    "views": None,
                    "upload_date": None,
                    "duration_seconds": None,
                    "description": None,
                    "thumbnail": None,
                    "like_count": None,
                    "comment_count": None,
                    "channel_subscribers": None,
                    "tags": None
                })

            all_rows.append(row)

        # Save progress after each channel
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

        temp_df = pd.DataFrame(all_rows)

        if os.path.exists(OUTPUT_FILE):

            old_df = pd.read_csv(OUTPUT_FILE)

            temp_df = pd.concat([old_df, temp_df], ignore_index=True)

            temp_df.drop_duplicates(subset=["video_id"], inplace=True)

        temp_df.to_csv(OUTPUT_FILE, index=False)

        print(f"✅ Saved progress ({len(temp_df)} videos)")

    print("\n" + "=" * 70)
    print("Scraping Completed!")

    print(f"Total Videos Saved: {len(temp_df)}")


if __name__ == "__main__":

    scrape_all()