//canSum(Targetsum, array of numbers)
//Recursive
// const canSum = (targetSum, numbers) => {
//     if (targetSum == 0) return true;
//     if (targetSum < 0) return false;
//     for (let num of numbers){
//         const remainder = targetSum - num;
//         if (canSum(remainder, numbers) == true) {
//             return true;
//         }
//     }
//     return false;
// };
// console.log(canSum(7, [7,14]));
//time complexity o(n^m) o(n^(m/min(numbers))) space = o(m)

// const canSum = (targetSum, numbers, memo = {0:true}) => {
//     if (targetSum in memo) return memo[targetSum]
//     if (targetSum < 0) return false;
//     for (let num of numbers){
//         const remainder = targetSum - num;
//         if (canSum(remainder, numbers, memo) == true) {
//             memo[targetSum] = true
//             return true;
//         }
//     }
//     memo[targetSum] = false
//     return false;
// };
// console.log(canSum(7, [7,14]));
//time o(m *n) space o(m)

//Iterative
// const canSum = (targetSum, numbers) => {
//     const table = Array(targetSum + 1).fill(false);
//     table[0] = true;
//     for (let i = 0; i <= targetSum; i++){
//         if (table[i] == true){
//             for (let num of numbers){
//                 table[i + num] = true;
//             }
//         }
//     }
//     return table[targetSum];
// };

// console.log(canSum(7, [2,4]));
//time: o(n*m) space: o(m)
