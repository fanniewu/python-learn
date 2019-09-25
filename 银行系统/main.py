'''
对象：人 User
属性：姓名，身份证号，电话，卡（多张卡，用字典存储 {卡号:卡对象, ......}）
行为：插卡，输入信息，退卡

对象：卡 Card
属性：账号，密码，余额，是否锁定
行为：无

对象：提款机 ATM
属性：系统账号，系统密码，余额，是否正常
行为：
    开机界面，欢迎界面，操作界面
    修改系统密码，提额
    开户，查询，存款，取款，转帐，改密，锁定，解锁，注销，补卡，退卡

对象：银行(单例类） Bank
属性：用户字典（{身份证号:用户对象, ......}）
行为：
'''
from 银行系统.atm import ATM

atmMachine = ATM()
atmMachine.money = 1000;

def main():
    while True:
        atmMachine.atmInitView()
        optionstr = input("请输入操作：")

        if optionstr == "11":
            res = atmMachine.checkPasswd()
            if not res:
                welcome()
        if optionstr == "22":
            atmMachine.shutdown()
            break
        if optionstr == "33":
            atmMachine.addMoney()
        if optionstr == "44":
            atmMachine.changeATMPasswd()

def welcome():
    while True:
        atmMachine.welcomeView()
        optionstr = input("请输入操作：")
        if optionstr == "111":
            atmMachine.readCard()
        if optionstr == "222":
            break

if __name__ == '__main__':
    main()