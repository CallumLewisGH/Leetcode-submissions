/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var hash_map = new Map();
    len = nums.length

    for (let index=0; index < len; index++){
        var itemIndex = hash_map.get(nums[index]);
        if (itemIndex > -1){
            return [index, itemIndex]
        }

        else {
            hash_map.set(target - nums[index], index)
        }
    }
    
};