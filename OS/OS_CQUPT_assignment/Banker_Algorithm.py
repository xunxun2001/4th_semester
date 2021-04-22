def main():
    resources = int(input("请输入资源数目 : "))
    processes = int(input("请输入进程数目 : "))
    max_resources = [int(i) for i in input("请输入最大资源数 : ").split()]

    print("\n-- 为每一个进程分配的资源 --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    print("\n-- 每一个进程的最大资源 --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\n总共的分配资源 : {allocated}")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"总共的可用资源 : {available}\n")

    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"进程 {i + 1} 正在执行")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("未能处于安全状态")
            break

        print(f"处于安全状态\n可用资源 : {available}\n")


if __name__ == '__main__':
    main()