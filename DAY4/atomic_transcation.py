from copy import deepcopy


class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass


batch_list = [{"acc": "ACC01", "type": "deposit", "amt": 150.0},{"acc": "ACC02", "type": "withdraw", "amt": 50.0}]
accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = "transactions.log"

def process_transaction_batch(accounts, batch_list, log_path):
    copied_accounts = deepcopy(accounts)
    
    try:
        
        for transaction in batch_list:
            acc = transaction["acc"]
            transaction_type = transaction["type"]
            amount = transaction["amt"]

            if acc not in accounts:
                raise AccountNotFoundError(f"Account {acc} not found !")

            if transaction_type not in ["deposit", "withdraw"]:
                raise InvalidTransactionError(f"Invalid transaction type  !")

            if amount <=0:
                raise InvalidTransactionError(f"Transaction amount must be positive")

            if transaction_type == "withdraw" and accounts[acc] < amount :
                raise OverdraftError(f'Insufficient funds. Account {acc} has balance {accounts["acc"]}, requested {amount}')

            if transaction_type == "deposit":
                accounts[acc] += amount

            elif transaction_type == "withdraw":
                accounts[acc] -= amount
                
        with open(log_path, "a") as file:
            file.write(f"[SUCCESS] Batch Completed.")
            
        return accounts
    except Exception as e:
        accounts.clear()
        accounts.update(copied_accounts)
        
        with open(log_path, "a") as file: file.write( f"[ROLLBACK] Batch aborted: " f"{type(e).__name__} - {e}\n" )

        raise

accounts = process_transaction_batch(
    accounts, batch_list, "transactions.log"
)

print(accounts)