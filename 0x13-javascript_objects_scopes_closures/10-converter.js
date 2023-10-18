#!/usr/bin/node
exports.converter = function (base) {
  return (nums) => {
    return nums.toString(base);
  };
};
