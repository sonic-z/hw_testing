def vote(votes):
    # your code
    votes_count = []
    for n in votes:
        votes_count.append(votes.count(n))
    votes_dict = {k: v for k, v in zip(votes, votes_count)}
    max_count = 0
    ele = None
    for k, v in votes_dict.items():
        if max_count < v:
            ele = k
            max_count = v
    return ele


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))