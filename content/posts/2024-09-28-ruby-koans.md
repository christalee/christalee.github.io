title: What is the sound of one gem shining?
tags: ruby, programming

These past couple of weeks I've been learning [Ruby](https://www.ruby-lang.org/en/), a language with a design philosophy similar to [Python](https://www.python.org/): high-level code that's easy to read and write. I started with the classic beginner's text, [Why's (Poignant) Guide to Ruby](https://poignant.guide/book/), a gonzo adventure through the language, but tapped out partway through Chapter 5, when they introduce the syntax `class << LotteryDraw` which uses a concatenation operator to create a class method inside `LotteryDraw`. This seemed pretty obscure to me, so I went looking for a more germane resource: a cheatsheet for Pythonistas coming to Ruby. I found a straight [Ruby cheatsheet](https://www.codecademy.com/learn/learn-ruby/modules/learn-ruby-introduction-to-ruby-u/cheatsheet) on Codecademy, and decided to work through their free course [Learn Ruby](https://www.codecademy.com/enrolled/courses/learn-ruby). I also decided to test my knowledge by working through [Ruby Koans](https://github.com/edgecase/ruby_koans), a tour of the language features via tests, where you practice the TDD mantra "red, green, refactor". Which is to say: the tests are written, but failing; it's up to you to correct them so they pass, and then optionally refactor them to be more robust.

Coming from Python, I initially struggled with the parts of the syntax which are just similar enough but different. For example, in Ruby, only `false` and `nil` are falsy; `[], {}, "", 0` are all truthy. Or for iterable slicing, what I would write in Python as `iterable[start:finish:step]` is in Ruby `iterable[start, length_of_slice]`, e.g `"string"[2, 3]` gives `"rin"`. Or you can use a range, `"string"[2..4]` also gives `"rin"`. (I have yet to decide whether I favor the two-dot or three-dot syntax for ranges - the first is inclusive, the second is exclusive. Pretty sure I should pick one, for my sanity!)

As an aide memoire for myself and anyone else coming to Ruby in the year 2024, here are some of the trickiest corners of the syntax I've found. (Note that they use a custom assert method; see `neo.rb` in Ruby Koans for details.)

```ruby
# Strings, arrays, and hashes are compared by value (hashes are unordered); 
# TODO understand how comparisons are made for objects

# Flexible quotes, where you prefix % and use any delimiter for the 
# beginning and end of the string
long_string = %{
It was the best of times,
It was the worst of times.
}

assert_equal 3, long_string.lines.count

# Something called documents, where you prefix << and use any delimiter for
# the beginning and end of a multi-line string (must start on a new line!)
long_string = <<EOS
It was the best of times,
It was the worst of times.
EOS

assert_equal 2, long_string.lines.count

# For string concatenation, += does not modify the original string 
# but << does 🤯
original_string = "Hello, "
hi = original_string
there = "World"

hi += there
assert_equal "Hello, ", original_string

hi = original_string
hi << there
assert_equal "Hello, World", original_string

# Double-quoted strings interpret escape characters but single-quoted 
# strings do not, except sometimes; double-quoted strings interpolate 
# variables but single-quoted strings do not
string = "\n"
assert_equal 1, string.size

string = '\n'
assert_equal 2, string.size

string = '\\\''
assert_equal 2, string.size
assert_equal "\\'", string

# Less surprising but good to know: Python's 
# 'delimiter.join(array_of_str)' is Ruby's 'array_of_str.join(delimiter)'
words = ["Now", "is", "the", "time"]
assert_equal "Now is the time", words.join(" ")

# Symbols are prefixed by :, can contain spaces via double quotes, are not 
# strings, are immutable, can be interpolated (!), and are somehow "cheaper" 
# than strings. So they are preferred when passing names around.
symbol = :"cats #{value} dogs"
assert_equal :"cats and dogs", symbol

# This is truly wild - you can index 1 past the last index in an array 
# without causing an error. The only way this makes sense to me is if you 
# can ask for a negative slice, but array[4, -2] is apparently not valid. 
# Asking for a slice that goes past the end of the array does not error, either.
array = [:peanut, :butter, :and, :jelly]
assert_equal [:peanut, :butter], array[0,2]
assert_equal [], array[4,0]
assert_equal [], array[4,100]
assert_equal nil, array[4, -2]
assert_equal nil, array[5,0]

# Ruby has a handy '*' syntax when doing parallel assignment, 
# like '...rest' destructuring in JavaScript
first_name, *last_name = ["John", "Smith", "III"]
assert_equal "John", first_name
assert_equal ["Smith", "III"], last_name

# nil can be converted to the empty string and inspected
assert_equal "", nil.to_s
assert_equal "nil", nil.inspect

# nil is also the result of accessing a key not in the hash via brackets 
# if no default is given, but an error is raised when using fetch
hash = { :one => "uno", :two => "dos" }
assert_equal nil, hash[:doesnt_exist]
assert_raise(KeyError) do
  hash.fetch(:doesnt_exist)
end

# Using a mutable object as the default value is fraught!
hash = Hash.new([])
hash[:one] << "uno"
hash[:two] << "dos"

assert_equal ["uno", "dos"], hash[:one]
assert_equal ["uno", "dos"], hash[:two]
assert_equal ["uno", "dos"], hash[:three]

assert_equal true, hash[:one].object_id == hash[:two].object_id

# Instead, use a block:
hash = Hash.new {|hash, key| hash[key] = [] }
hash[:one] << "uno"
hash[:two] << "dos"

assert_equal ["uno"], hash[:one]
assert_equal ["dos"], hash[:two]
assert_equal [], hash[:three]

# You can make global methods private but without self, they won't
# be protected (I'm not too hot on self, generally speaking.)
def my_private_method
  "a secret"
end
private :my_private_method

assert_equal "a secret", my_private_method
assert_raise(NoMethodError) do
  self.my_private_method
end

# Inheritance in nested classes is a bit tricky. Just keep it in mind.
class Animal
  LEGS = 4
  def legs_in_animal
    LEGS
  end
end
  
class MyAnimals
  LEGS = 2

  class Bird < Animal
    def legs_in_bird
      LEGS
    end
  end
end

assert_equal 2, MyAnimals::Bird.new.legs_in_bird

class MyAnimals::Oyster < Animal
  def legs_in_oyster
    LEGS
  end
end

assert_equal 4, MyAnimals::Oyster.new.legs_in_oyster

# Compared to Python's 're.match' object, Ruby is a bit more loosey-goosey.
# Where do these (global?) '$variables' come from?
assert_equal "Gray, James", "Name:  Gray, James"[/(\w+), (\w+)/]
assert_equal "Gray", $1
assert_equal "James", $2

# I just don't like 'unless' as a control statement. Python 'continue' 
# is Ruby 'next if condition'.

# I'm intrigued by the Ruby convention of ending methods that return 
# booleans with ? (obj.is_a?(class)) and methods that modify their 
# callers in-place with ! (string.gsub!(regexp) { block }) and methods 
# that assign values with = (are there any built-in examples?). I'm bemused
# by the theory that parentheses are optional; I think I will keep them 
# in for clarity where possible. (Obviously I will follow the conventions of 
# the codebase I'm working in. I hope there is good linting support for that.)

# Ruby has both 'collect' and 'map' (synonyms). It also has 'select' and
# 'find_all' (synonyms for 'filter'). It calls 'reduce' as 'inject'. 
# These are all array methods.
result = [2, 3, 4].inject(0) { |sum, item| sum + item }
assert_equal 9, result

result2 = [2, 3, 4].inject(1) { |product, item| product * item }
assert_equal 24, result2

# I don't understand the use of 'yield'. It makes sense when I read it, 
# more or less, but I can't imagine wielding it effectively. 
# (I am fuzzy on Python 'yield' (generators) as well.)

# I'm also not too clear on class vs. instance methods. I'm beginning to 
# understand when I would use one vs. the other but I would like 
# more examples to cement that. 
```