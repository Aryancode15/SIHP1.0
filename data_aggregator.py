from datetime import datetime, timedelta

def fetch_and_classify_data():
    # Sample mock data
    sample_data = [
        {
            "source": "Twitter",
            "title": "Heavy flood reported in Kerala",
            "content": "Water levels rose up to 4 feet...",
            "timestamp": (datetime.now() - timedelta(hours=1)).isoformat(),
            "location": "Kerala, India",
            "type": "flood",
            "url": "https://news.example.com/flood-kerala"
        },
        {
            "source": "NewsAPI",
            "title": "Earthquake tremors shake Tokyo",
            "content": "Magnitude 5.2 tremors recorded...",
            "timestamp": (datetime.now() - timedelta(hours=3)).isoformat(),
            "location": "Tokyo, Japan",
            "type": "earthquake",
            "url": "https://news.example.com/earthquake-tokyo"
        }
    ]
    return sample_data
