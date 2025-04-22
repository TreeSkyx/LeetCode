/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  n_arr = arr;
  return (n_arr = n_arr.map(fn));
};
