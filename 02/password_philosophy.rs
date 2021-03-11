use std::fs;

struct Password {
	pw: String,
	letter: char,
	min: usize,
	max: usize
}

fn is_valid_p1(pw: &Password) -> bool {
	let occ: usize = pw.pw.matches(pw.letter).count();
	return pw.min <= occ && occ <= pw.max;
}


fn is_valid_p2(pw: &Password) -> bool {
	let lst: Vec<char> = pw.pw.chars().collect();
	return (lst[pw.min-1] == pw.letter) != (lst[pw.max-1] == pw.letter)
}

fn main() {
	let mut pw_data = Vec::<Password>::new();

	let file_content = fs::read_to_string("input.txt")
		.expect("Something went wrong reading the file");

	for line in file_content.split("\n") {
		
		let line: Vec<&str> = line.split_ascii_whitespace().collect();
		if line.is_empty() {
			continue;
		}

		pw_data.push(Password {
			pw: match line.last(){
				Some(v) => String::from(*v),
				None => String::new()
			},
			
			letter: line[1].chars().next().unwrap(),
			
			min: match line[0].split("-").nth(0) {
				Some(v) => v.parse::<usize>().unwrap(),
				None => 1
			},
			
			max: match line[0].split("-").nth(1) {
				Some(v) => v.parse::<usize>().unwrap(),
				None => 1
			},
		});
	}

	let mut p1_result: usize = 0;
	let mut p2_result: usize = 0;


	for pw in pw_data {
		if is_valid_p1(&pw) {
			p1_result += 1;
		}
		if is_valid_p2(&pw) {
			p2_result += 1;
		}
	}

	println!("Part 1: {}\nPart 2: {}", p1_result, p2_result);
}