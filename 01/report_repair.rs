use std::fs;

fn combinations(l: &Vec<u32>, count: u32) -> Vec<Vec<u32>> {
	let mut result = Vec::<Vec<u32>>::new();
	for a in l {
		for b in l {
			if count < 3 {
				let vec = vec![*a,*b];
				result.push(vec);
				continue;
			}
			for c in l {
				let vec = vec![*a,*b,*c];
				result.push(vec);
			}
		}
	}
	return result;
}


fn get_summands(l: &Vec<u32>, result: u32, summand_count: u32) -> Option<Vec<u32>> {
	for comb in combinations(l, summand_count) {
		let sum: u32 = comb.iter().sum();
		if sum == result {
			return Some(comb);
		}
	}
	return None;
}

fn product(factors: &Vec<u32>) -> u32 {
	let mut acc: u32 = 1;
	for f in factors {
		acc *= f;
	}
	return acc;
}

fn main() {
	let file_content = fs::read_to_string("input.txt")
		.expect("Something went wrong reading the file");

	let numbers = file_content
		.split_ascii_whitespace()
		.map(|e| e.parse::<u32>().unwrap())
		.collect();

	let p1_summands = match get_summands(&numbers, 2020, 2){
		Some(vec) => vec,
		None => Vec::<u32>::new()
	};

	let p2_summands = match get_summands(&numbers, 2020, 3){
		Some(vec) => vec,
		None => Vec::<u32>::new()
	};	

	let p1_result = product(&p1_summands);
	let p2_result = product(&p2_summands);

	println!("Part 1: {}\nPart 2: {}", p1_result, p2_result);
}