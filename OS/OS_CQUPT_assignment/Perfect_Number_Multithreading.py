'''
实现多线程程序测试一个数是否是完全数
实现一个多线程程序测试一个数是否是完全数。如果一个数N的所有因数（不包括N本身）的和还是N，则N是一个完全数，如6和28，输入是一个整数N，如果N是完全数则输出true，否则输出false。主程序从命令行读取数字N和P，创建P个线程，将1~N这N个数分给各个线程，保证两个线程不会分到相同的数。每个线程判断这些树是不是N的因数，如果是，那么放到一个共享的缓冲区中。在父进程中用合适的同步方法等待所有的线程执行完毕后，判断N是否是完全数，即判断是否N的所有因数之和还是N（提示：你可以将测试的数限定在1至N的平方根来加速计算过程。）
'''


import threading
rs = [] 
lock = threading.RLock()
class Isprime(threading.Thread):

    def __init__(self,num,name=None):
        threading.Thread.__init__(self) #不要忘记
        self.num = num
        self.isstop = False
    
    def run(self):
        global rs,lock          
        isprime = False     
        m = self.num 
        sums = 0
        for i in range(1,int(math.sqrt(m))+1):
            if m%i==0:
                sums += i
                if i>1 and i!=m//i:
                    sums += m//i
        if sums==m:
            isprime = True
            break 
        lock.acquire() 
        if not isprime:
            rs.append(m)
        lock.release()
        
 def perfect(num):

 
 
                
def main():
    global rs 
    threads = []
    #装载线程
    for i in range(2,101): 
        threads.append(Isprime(i))
    #启动线程
    for x in threads:
        x.start()
    #阻塞线程直到结束
    for s in threads:
        x.join()
    #打印结果    
    print rs 
    print len(rs)  
 
 
if __name__=='__main__':
    main()
