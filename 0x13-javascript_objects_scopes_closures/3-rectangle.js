#!/usr/bin/node
//class Rectangle that defines a rectangle.
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = ('X'.repeat(this.width) + '\n').repeat((this.height - 1));
    rect += ('X'.repeat(this.width));
    console.log(rect);
  }
};
