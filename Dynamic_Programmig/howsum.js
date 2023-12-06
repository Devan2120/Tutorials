//howSum(targetSum, numbers)
//Recursive
// const howSum = (targetSum, numbers) => {
//     if (targetSum == 0) return [];
//     if (targetSum < 0) return null;
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         const remainderResult = howSum(remainder, numbers);
//         if (remainderResult != null){
//             return [ ...remainderResult, num];
//         }
//     }
//     return null;
// };

// console.log(howSum(7, [2,4]));
//time complexity o(n^m*m)(copying operation takes o(m) which is done n^m times)
//space o(m)

// const howSum = (targetSum, numbers, memo = {0:[]}) => {
//     if (targetSum in memo) return memo[targetSum];
//     if (targetSum < 0) return null;
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         const remainderResult = howSum(remainder, numbers, memo);
//         if (remainderResult != null){
//             memo[targetSum] = [ ...remainderResult, num];
//             return memo[targetSum];
//         }
//     }
//     memo[targetSum] = null;
//     return null;
// };

// console.log(howSum(300, [7,1]));
// time : o(n*m*m) space o(m*m)(each key may have an array of length max m)

//Iterative
// const howSum = (targetSum, numbers) => {
//      const table = Array(targetSum + 1).fill(null);
//      table[0] = [];
//      for (let i = 0; i <= targetSum; i++){
//         if (table[i] != null){
//             for (let num of numbers){
//                 table[i + num] = [...table[i], num];
//             }
//         }
//      }
//      return table[targetSum];
// };

// console.log(howSum(7, [2,4]));
//time: (m*n*m) space:(m*m)