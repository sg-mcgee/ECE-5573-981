{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "id": "a4563bef-0a5c-44c6-a16b-f20976d45a82",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a4563bef-0a5c-44c6-a16b-f20976d45a82",
        "outputId": "83e09053-7bf0-4e31-9e7a-96f652a521cd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: yfinance in /usr/local/lib/python3.11/dist-packages (0.2.52)\n",
            "Requirement already satisfied: pandas>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2.2.2)\n",
            "Requirement already satisfied: numpy>=1.16.5 in /usr/local/lib/python3.11/dist-packages (from yfinance) (1.26.4)\n",
            "Requirement already satisfied: requests>=2.31 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2.32.3)\n",
            "Requirement already satisfied: multitasking>=0.0.7 in /usr/local/lib/python3.11/dist-packages (from yfinance) (0.0.11)\n",
            "Requirement already satisfied: lxml>=4.9.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (5.3.1)\n",
            "Requirement already satisfied: platformdirs>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from yfinance) (4.3.6)\n",
            "Requirement already satisfied: pytz>=2022.5 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2025.1)\n",
            "Requirement already satisfied: frozendict>=2.3.4 in /usr/local/lib/python3.11/dist-packages (from yfinance) (2.4.6)\n",
            "Requirement already satisfied: peewee>=3.16.2 in /usr/local/lib/python3.11/dist-packages (from yfinance) (3.17.9)\n",
            "Requirement already satisfied: beautifulsoup4>=4.11.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (4.13.3)\n",
            "Requirement already satisfied: html5lib>=1.1 in /usr/local/lib/python3.11/dist-packages (from yfinance) (1.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4>=4.11.1->yfinance) (2.6)\n",
            "Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4>=4.11.1->yfinance) (4.12.2)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.11/dist-packages (from html5lib>=1.1->yfinance) (1.17.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.11/dist-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.3.0->yfinance) (2.8.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.3.0->yfinance) (2025.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.31->yfinance) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.31->yfinance) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.31->yfinance) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.31->yfinance) (2025.1.31)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy>=1.23.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (1.26.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install yfinance # uncomment these to install missing packages if they are not already installed\n",
        "!pip install pandas"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "33c9d138-5310-47f8-b2cd-1a28f97c4fb4",
      "metadata": {
        "id": "33c9d138-5310-47f8-b2cd-1a28f97c4fb4"
      },
      "outputs": [],
      "source": [
        "import yfinance as yf\n",
        "import pandas as pd\n",
        "\n",
        "def get_price(tick,start='2022-10-01',end=None):\n",
        "    return yf.Ticker(tick).history(start=start,end=end)['Close']\n",
        "\n",
        "def get_prices(tickers,start='2022-10-01',end=None):\n",
        "    df=pd.DataFrame()\n",
        "    for s in tickers:\n",
        "        df[s]=get_price(s,start,end)\n",
        "    return df\n",
        "\n",
        "def get_price_local(tick,csv_file,start='2022-10-01',end=None):\n",
        "    df = pd.read_csv(csv_file, parse_dates=['Date'], index_col='Date')\n",
        "    return df[tick]\n",
        "\n",
        "def get_prices_local(tickers,csv_file,start='2022-10-01',end=None):\n",
        "    df=pd.DataFrame()\n",
        "    for s in tickers:\n",
        "        df[s]=get_price(s,csv_file,start,end)\n",
        "    return df\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "quick-cartoon",
      "metadata": {
        "id": "quick-cartoon"
      },
      "source": [
        "# Prepare training and testing data sets"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "designed-storm",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "designed-storm",
        "outputId": "607af38f-37a3-4b8a-e0dd-ac5dc7352cb5"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "YFRateLimitError",
          "evalue": "Too Many Requests. Rate limited. Try after a while.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mYFRateLimitError\u001b[0m                          Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-fe3fb51a3fd7>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mend_date_train\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'2024-6-30'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m \u001b[0mX_train\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mget_prices\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfeature_stocks\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstart_date_train\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mend_date_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0my_train\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mget_prices\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mpredict_stock\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstart_date_train\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mend_date_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-4-2e8616f85288>\u001b[0m in \u001b[0;36mget_prices\u001b[0;34m(tickers, start, end)\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0mdf\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0ms\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtickers\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m         \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mget_price\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-4-2e8616f85288>\u001b[0m in \u001b[0;36mget_price\u001b[0;34m(tick, start, end)\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mget_price\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtick\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'2022-10-01'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0myf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTicker\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtick\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhistory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Close'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mget_prices\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtickers\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'2022-10-01'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/utils.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m         \u001b[0;32mwith\u001b[0m \u001b[0mIndentationContext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 104\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    105\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    106\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'Exiting {func.__name__}()'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/base.py\u001b[0m in \u001b[0;36mhistory\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     79\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog_indent_decorator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mhistory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 81\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_lazy_load_price_history\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhistory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     82\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m     \u001b[0;31m# ------------------------\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/base.py\u001b[0m in \u001b[0;36m_lazy_load_price_history\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     85\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_lazy_load_price_history\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     86\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_price_history\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 87\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_price_history\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mPriceHistory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mticker\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_ticker_tz\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mproxy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     88\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_price_history\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     89\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/base.py\u001b[0m in \u001b[0;36m_get_ticker_tz\u001b[0;34m(self, proxy, timeout)\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    102\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mtz\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 103\u001b[0;31m             \u001b[0mtz\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_fetch_ticker_tz\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mproxy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    104\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    105\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_valid_timezone\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtz\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/utils.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m         \u001b[0;32mwith\u001b[0m \u001b[0mIndentationContext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 104\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    105\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    106\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'Exiting {func.__name__}()'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/base.py\u001b[0m in \u001b[0;36m_fetch_ticker_tz\u001b[0;34m(self, proxy, timeout)\u001b[0m\n\u001b[1;32m    124\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    125\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 126\u001b[0;31m             \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcache_get\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mproxy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    127\u001b[0m             \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    128\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mYFRateLimitError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/data.py\u001b[0m in \u001b[0;36mwrapped\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m     28\u001b[0m         \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0marg\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0marg\u001b[0m \u001b[0;32min\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m         \u001b[0mkwargs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0mv\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mv\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     31\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m     \u001b[0;31m# copy over the lru_cache extra methods to this wrapper to be able to access them\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/data.py\u001b[0m in \u001b[0;36mcache_get\u001b[0;34m(self, url, user_agent_headers, params, proxy, timeout)\u001b[0m\n\u001b[1;32m    402\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mlru_cache\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmaxsize\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcache_maxsize\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    403\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcache_get\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muser_agent_headers\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m30\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 404\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muser_agent_headers\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    405\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    406\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_get_proxy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/utils.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m         \u001b[0;32mwith\u001b[0m \u001b[0mIndentationContext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 104\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    105\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    106\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'Exiting {func.__name__}()'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/data.py\u001b[0m in \u001b[0;36mget\u001b[0;34m(self, url, user_agent_headers, params, proxy, timeout)\u001b[0m\n\u001b[1;32m    333\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog_indent_decorator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    334\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muser_agent_headers\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m30\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 335\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrequest_method\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_session\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muser_agent_headers\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0muser_agent_headers\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mproxy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mproxy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    336\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    337\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog_indent_decorator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/utils.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m         \u001b[0;32mwith\u001b[0m \u001b[0mIndentationContext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 104\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    105\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    106\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'Exiting {func.__name__}()'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/yfinance/data.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, url, request_method, user_agent_headers, body, params, proxy, timeout)\u001b[0m\n\u001b[1;32m    395\u001b[0m             \u001b[0;31m# Raise exception if rate limited\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus_code\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m429\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 397\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mYFRateLimitError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    398\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    399\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mYFRateLimitError\u001b[0m: Too Many Requests. Rate limited. Try after a while."
          ]
        }
      ],
      "source": [
        "feature_stocks=['tsla','meta','goog','amzn','nflx','gbtc','gdx','intc','dal','c']\n",
        "predict_stock='msft'\n",
        "\n",
        "# training set\n",
        "start_date_train='2023-1-01'\n",
        "end_date_train='2024-6-30'\n",
        "\n",
        "#Get training set through yfinance\n",
        "#X_train=get_prices(feature_stocks,start=start_date_train,end=end_date_train)\n",
        "#y_train=get_prices([predict_stock],start=start_date_train,end=end_date_train)\n",
        "#Get training set locally through csv (yfinance causing issues)\n",
        "X_train=get_prices(feature_stocks,,start=start_date_train,end=end_date_train)\n",
        "y_train=get_prices([predict_stock],start=start_date_train,end=end_date_train)\n",
        "\n",
        "# testing set\n",
        "start_date_test='2024-11-01'\n",
        "end_date_test='2024-12-31'\n",
        "X_test=get_prices(feature_stocks,start=start_date_test,end=end_date_test)\n",
        "y_test=get_prices([predict_stock],start=start_date_test,end=end_date_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "id": "former-sodium",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "former-sodium",
        "outputId": "0e981786-153a-4243-d6aa-affdc8a73442"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'X_train' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-931765772341>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mX_train\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m: name 'X_train' is not defined"
          ]
        }
      ],
      "source": [
        "X_train"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "round-stadium",
      "metadata": {
        "id": "round-stadium",
        "outputId": "f87227d4-cbdc-463c-94cb-3428b676778e"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>msft</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2023-01-03 00:00:00-05:00</th>\n",
              "      <td>235.711700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2023-01-04 00:00:00-05:00</th>\n",
              "      <td>225.400925</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2023-01-05 00:00:00-05:00</th>\n",
              "      <td>218.720551</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2023-01-06 00:00:00-05:00</th>\n",
              "      <td>221.298233</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2023-01-09 00:00:00-05:00</th>\n",
              "      <td>223.452896</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2024-06-24 00:00:00-04:00</th>\n",
              "      <td>445.971924</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2024-06-25 00:00:00-04:00</th>\n",
              "      <td>449.239441</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2024-06-26 00:00:00-04:00</th>\n",
              "      <td>450.444855</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2024-06-27 00:00:00-04:00</th>\n",
              "      <td>451.132233</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2024-06-28 00:00:00-04:00</th>\n",
              "      <td>445.254639</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>374 rows × 1 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                                 msft\n",
              "Date                                 \n",
              "2023-01-03 00:00:00-05:00  235.711700\n",
              "2023-01-04 00:00:00-05:00  225.400925\n",
              "2023-01-05 00:00:00-05:00  218.720551\n",
              "2023-01-06 00:00:00-05:00  221.298233\n",
              "2023-01-09 00:00:00-05:00  223.452896\n",
              "...                               ...\n",
              "2024-06-24 00:00:00-04:00  445.971924\n",
              "2024-06-25 00:00:00-04:00  449.239441\n",
              "2024-06-26 00:00:00-04:00  450.444855\n",
              "2024-06-27 00:00:00-04:00  451.132233\n",
              "2024-06-28 00:00:00-04:00  445.254639\n",
              "\n",
              "[374 rows x 1 columns]"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "y_train"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "written-antibody",
      "metadata": {
        "id": "written-antibody"
      },
      "source": [
        "# Convert training and testing data into numpy array"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "hired-findings",
      "metadata": {
        "id": "hired-findings"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "X_train=np.array(X_train)\n",
        "y_train=np.array(y_train)\n",
        "X_test=np.array(X_test)\n",
        "y_test=np.array(y_test)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "helpful-metadata",
      "metadata": {
        "id": "helpful-metadata"
      },
      "source": [
        "# Use linear regression to predict msft stock price from the other stocks' prices"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "southeast-equivalent",
      "metadata": {
        "id": "southeast-equivalent"
      },
      "source": [
        "## 1. Append a dummy feature to both X_train and X_test"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "id": "connected-nursing",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "connected-nursing",
        "outputId": "c8cb6278-3751-419c-f274-43ccbad9f2e9"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'np' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-f764f0073357>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Your solution here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mX_train_shape\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mX_train_ones\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mones\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_train_shape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mX_test_shape\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_test\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mX_test_ones\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mones\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_test_shape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'np' is not defined"
          ]
        }
      ],
      "source": [
        "# Your solution here\n",
        "X_train_shape = np.shape(X_train)\n",
        "X_train_ones = np.ones(X_train_shape[0],1)\n",
        "X_test_shape = np.shape(X_test)\n",
        "X_test_ones = np.ones(X_test_shape[0],1)\n",
        "\n",
        "X_train = np.append(X_train,X_train_ones,axis=1)\n",
        "X_test =  np.append(X_test,X_test_ones,axis=1)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "romance-pharmaceutical",
      "metadata": {
        "id": "romance-pharmaceutical"
      },
      "source": [
        "## 2. Find the best linear regression model based on your training data ($w=(X X')^{-1} X y$)\n",
        "### Note that you may need to transpose the matrices to make things work\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "emotional-vacation",
      "metadata": {
        "id": "emotional-vacation"
      },
      "outputs": [],
      "source": [
        "# Your solution here\n",
        "XT = np.linalg.inv(X_train)\n",
        "X_mult_XT_train = np\n",
        "weights = np.linalg.inv(X_train)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "understood-vacation",
      "metadata": {
        "id": "understood-vacation"
      },
      "source": [
        "## 3. Report your training and testing error\n",
        "### How far your prediction from the actual price. Compute the mean square error for both training and testing"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "crude-breeding",
      "metadata": {
        "id": "crude-breeding"
      },
      "outputs": [],
      "source": [
        "# Your solution here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "stainless-circuit",
      "metadata": {
        "id": "stainless-circuit"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "sticky-portland",
      "metadata": {
        "id": "sticky-portland"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.12"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}