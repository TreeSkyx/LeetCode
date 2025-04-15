int majorityElement(int* nums, int numsSize)
{
    int me = 0, count = 0;
    for (int i = 0; i < numsSize; i++){
        if (count == 0){
            me = nums[i];
        }
        if (nums[i] == me){
            count++;
        } else {
            count--;
        }
    }
    return me;
}
