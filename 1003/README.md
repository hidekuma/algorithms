# 해결포인트
일단 이 문제는 속도제한만 잘 처리하면 쉽게 풀수 있었다.
0 과 1값이 각각 몇 번 출력되는지 합해보면 받는 0, 1을 제외한 입력값을 받을 경우, 그 결과가 피보나치 수열로 나타난다.(조금 신기)
예를 들어서, 3이 들어오면 [0, 1, 1, 2, 3, 5]과 같은 피보나치 수열의 2번 index와 3번 index 값이 답이 된다.
쓸데없는 연산은 줄이고 입력값이 커질때마다 그 증가수에 비례한 피보나치 수를 배열에 추가해 나가는 형식으로 코드를 짜면 해결할 수 있다.

위 내용이 잘 이해가 안간다면, 다음 코드를 런해보면 된다.
```python
def fibonacci_cnt(n, zero=0, one=0):
    if n == 0:
        #print(0)
        zero+=1
        return 0, zero, one
    elif n == 1:
        #print(1)
        one+=1
        return 1, zero, one
    else:
        fib1 = fibonacci_cnt(n-1)
        fib2 = fibonacci_cnt(n-2)
        zero += fib1[1]+fib2[1]
        one += fib1[2]+fib2[2]
        return fib1[0]+fib2[0], zero, one

inp = int(input())
print('--run--')
for _ in range(inp):
    n = int(input())
    rtn = fibonacci_cnt(n)
    print('%s %s' % (rtn[1], rtn[2]))
    print('-'*30)
```

## 문제
### [1003: 피보나치 함수](https://www.acmicpc.net/problem/1003)
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.
```c
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
```
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
- fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
- fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
- 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
- fibonacci(0)은 0을 출력하고, 0을 리턴한다.
- fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
- 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
- fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

### 출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

### 예제 입력
```
3
0
1
3
```

### 예제 출력
```
1 0
0 1
1 2
```
