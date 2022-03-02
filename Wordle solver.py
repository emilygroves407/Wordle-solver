{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0632594a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2b2f45a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#data set obtained from https://www.kaggle.com/bcruise/wordle-valid-words\n",
    "df = pd.read_csv('valid_solutions.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f953069e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#assign each letter from each wordto separate column with word as index\n",
    "for i in range(1,6):\n",
    "    df[f'index {i}']= df['word'].apply(lambda word: list(word)[i-1])\n",
    "df = df.set_index('word')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b5421844",
   "metadata": {},
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
       "      <th>index 1</th>\n",
       "      <th>index 2</th>\n",
       "      <th>index 3</th>\n",
       "      <th>index 4</th>\n",
       "      <th>index 5</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>aback</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>a</td>\n",
       "      <td>c</td>\n",
       "      <td>k</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abase</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>a</td>\n",
       "      <td>s</td>\n",
       "      <td>e</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abate</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>a</td>\n",
       "      <td>t</td>\n",
       "      <td>e</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abbey</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>e</td>\n",
       "      <td>y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abbot</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>o</td>\n",
       "      <td>t</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      index 1 index 2 index 3 index 4 index 5\n",
       "word                                         \n",
       "aback       a       b       a       c       k\n",
       "abase       a       b       a       s       e\n",
       "abate       a       b       a       t       e\n",
       "abbey       a       b       b       e       y\n",
       "abbot       a       b       b       o       t"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6b1166ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "#input for grey letters\n",
    "def grey():\n",
    "    \n",
    "    grey_letters = list(input(\"Grey letters:\").lower())\n",
    "    global df\n",
    "    \n",
    "    for letter in grey_letters:\n",
    "        df = df.replace(letter, np.nan).dropna(axis=0, how='any')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3747a2ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#input for green letters, if any\n",
    "def green():\n",
    "    \n",
    "    green_letters = []\n",
    "    green_pos = []\n",
    "    global df\n",
    "    \n",
    "    got_green = True\n",
    "    \n",
    "    while True:\n",
    "        any_green = ''\n",
    "        while any_green != 'y' and any_green != 'n':\n",
    "            any_green = input(\"Any (more) green letters?: y/n\").lower()\n",
    "        \n",
    "        if any_green == 'y':\n",
    "            green_letters.append(input('Green letter:'))\n",
    "            green_pos.append(input('Position (1-5):'))\n",
    "                    \n",
    "            df = df[df[f'index {int(green_pos[0])}'] == green_letters[0]]\n",
    "            \n",
    "            green_letters.pop()\n",
    "            green_pos.pop()\n",
    "            continue\n",
    "            \n",
    "        else:\n",
    "            got_green == False\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6436b258",
   "metadata": {},
   "outputs": [],
   "source": [
    "#input for yellow letters, if any\n",
    "def yellow():\n",
    "    \n",
    "    yellow_letters = []\n",
    "    yellow_pos = []\n",
    "    global df\n",
    "    \n",
    "    got_yellow = True\n",
    "    \n",
    "    \n",
    "    while True:\n",
    "        any_yellow = ''\n",
    "        while any_yellow != 'y' and any_yellow != 'n':\n",
    "            any_yellow = input(\"Any (more) yellow letters?: y/n\").lower()\n",
    "        \n",
    "        if any_yellow == 'y':\n",
    "            yellow_letters.append(input('Yellow letter:'))\n",
    "            yellow_pos.append(input('Position (1-5):'))\n",
    "            \n",
    "            df = df[~df[f'index {int(yellow_pos[0])}'].isin(yellow_letters)]\n",
    "            df = df[df.isin(yellow_letters).any(axis=1)]\n",
    "            \n",
    "            yellow_letters.pop()\n",
    "            yellow_pos.pop()\n",
    "            continue\n",
    "            \n",
    "        else:\n",
    "            got_yellow == False\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f48047b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#function to take results of each round (grey, green, yellow letters), update database\n",
    "#possible words, and return this together with the number of possibilities remaining\n",
    "def play_round():\n",
    "    grey()\n",
    "    green()\n",
    "    yellow()\n",
    "    \n",
    "    print(f'{len(df)} possible words remaining')\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
