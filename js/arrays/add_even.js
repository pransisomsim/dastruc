
// 4 + 2 + 4 + 92 = 102
const nums = [4, 11, 2, 4, 9, 73, 92, 55];

function is_even(num) {
  return num % 2 === 0;
}

function add_even(arr) {
  let value = 0;

  for (let i = 0; i < arr.length; i++) {
    if (is_even(arr[i])) {
      value += arr[i];
    }    
  }
  return value;
}

console.log(add_even(nums)); //output will be 102
