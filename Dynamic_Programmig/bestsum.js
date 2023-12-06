//bestSum(targetSum, numbers)
//Recursive
// const bestSum = (targetSum, numbers) => {
//     if (targetSum == 0) return [];
//     if (targetSum < 0) return null;
//     let shortestCombination = null;
//     for (let num of numbers) {
//         const remainder = targetSum -num;
//         const remainderCombination = bestSum(remainder, numbers);
//         if (remainderCombination != null) {
//             const combination = [ ...remainderCombination, num];
//             if (shortestCombination == null || combination.length < shortestCombination.length){
//                 shortestCombination = combination;
//             }
//         }
//     }

//     return shortestCombination;
// };

// console.log(bestSum(8,[1,4,5]))
//time : o(n^m*m) space: o(m*m) (shortestCombination)

// const bestSum = (targetSum, numbers, memo = {0:[]}) => {
//     if (targetSum in memo) return memo[targetSum];
//     if (targetSum < 0) return null;
//     let shortestCombination = null;
//     for (let num of numbers) {
//         const remainder = targetSum -num;
//         const remainderCombination = bestSum(remainder, numbers, memo);
//         if (remainderCombination != null) {
//             const combination = [ ...remainderCombination, num];
//             if (shortestCombination == null || combination.length < shortestCombination.length){
//                 shortestCombination = combination;
//             }
//         }
//     }
//     memo[targetSum] = shortestCombination;
//     return memo[targetSum];
// };

// console.log(bestSum(100,[1,4,5]))
// time : o(m*n*m) max values is targetSum(in case of -1) with max n branches with o(m) for copying
//space o(m*m)

//Iterative
// const bestSum = (targetSum, numbers) => {
//     const table = Array(targetSum + 1).fill(null);
//     table[0] = [];
//     for (let i = 0; i <= targetSum; i++){
//         if (table[i] != null){
//             for (let num of numbers){
//                 const combination = [...table[i], num];
//                 if (!table[i + num] || combination.length < table[i + num].length) {
//                     table[i + num] = combination;
//                 }
//             }
//         }
//     }
//     return table[targetSum];
// };

// console.log(bestSum(7, [5,4,3]));
//time: o(m*n*n) space:(m*m)

