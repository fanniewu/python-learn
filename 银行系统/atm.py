import time


class ATM(object):
    def __init__(self):
        self.account = "1"
        self.passwrd = "1"
        self.money = 0
        self.isActive = True

    def atmInitView(self):
        print("=========开机界面==========")
        print("=======输入系统用户========")
        print("=======输入系统密码========")
        print("====登录(11)  关机(22)=====")
        print("====提额(33)  改密(44)=====")

    def welcomeView(self):
        print("========欢迎界面==========")
        print("=======插卡（111）========")
        print("=======返回（222）========")

    def operationsView(self, name, cardID):
        print("===用户名：%s  卡号：%s=="%(name,cardID))
        print("====查询(1)   转账(2)=====")
        print("====存款(3)   取款(4)=====")
        print("==========退卡(5)=========")

    def checkPasswd(self):
        account = input("请输入系统账号：")
        passwd = input("请输入系统密码：")
        if account !=self.account or passwd != self.passwrd:
            print("账号或密码错误")
            return 1
        else:
            print("登录成功，正在启动……")
            time.sleep(2)


    def shutdown(self):
        # 数据持久化
        print("数据正在保存")

    def addMoney(self):
        money = int(input("请输入提额额度："))
        self.money += money
        if not self.isActive:
            self.isActive = True

    def changeATMPasswd(self):
        passwd = input("请输入原始密码：")
        if passwd != self.passwrd:
            print("密码错误，修改失败")
            return 1
        else:
            passwd1 = input("请输入新密码：")
            passwd2 = input("请再次输入新密码：")
            if passwd1 != passwd2:
                print("两次输入密码不同，修改失败")
                return
            else:
                self.passwrd = passwd2
                print("密码修改成功")

    def readCard(self):
        name = input("请插入卡(账户姓名)：")
        cardID = input("请插入卡(账号)：")
        self.operationsView(name, cardID)