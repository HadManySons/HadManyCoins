from HadManyCoinsPOC import HadManyCoins

def main():
    blockchain = HadManyCoins()
    t1 = blockchain.new_transaction("asdf", "fdsa", 1)
    blockchain.new_block(1)
    blockchain.new_block(2)
    print(blockchain.chain)

if __name__ == "__main__":
    main()
