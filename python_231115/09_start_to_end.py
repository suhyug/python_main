# # 방법1: 리스트의 첫 번째 요소와 마지막 요소의 합을 반환
nums = [int(i) for i in input().split()]
#값을 입력받아 리스트로 저장하는 일반적인 방법
start, *_, end = nums
#언더스코어는 언패킹
print(start + end)

# # 방법2: 리스트의 첫 번째 요소와 마지막 요소의 합을 반환
nums = [int(i) for i in input().split()]
print(nums[0] + nums[-1])

# # 방법3: 리스트의 첫 번째 요소와 마지막 요소의 합을 반환
# nums = [int(i) for i in input().split()]
# start_idx = 0
# end_idx = len(nums) -1
# print(nums[start_idx] + nums[end_idx])

# # 방법4: 리스트의 첫 번째 요소와 마지막 요소의 합을 반환
# nums = [int(i) for i in input().split()]
# print(nums.pop(0) + nums.pop())
#pop에 인자를 전달하지 않으면 기본 마지막 요소를 뽑아냄