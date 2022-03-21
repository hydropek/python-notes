{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac8c63d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269\n"
     ]
    }
   ],
   "source": [
    "cur = 1\n",
    "prev = 0\n",
    "limit = int(1e6)\n",
    "while cur < limit:\n",
    "    print(cur, end = ', ')\n",
    "    cur, prev = cur + prev, cur\n",
    "print(cur)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2970e62",
   "metadata": {},
   "outputs": [],
   "source": []
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
