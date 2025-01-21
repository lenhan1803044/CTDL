using DataStructures

mutable struct Queue
    elements::Deque{Any}  # Sử dụng Deque để lưu trữ phần tử
    Queue() = new(Deque{Any}())  # Khởi tạo hàng đợi rỗng
end

# Hàm thêm phần tử vào hàng đợi
function enqueue!(q::Queue, item)
    push!(q.elements, item)  # Thêm phần tử vào cuối deque
    println("Đã thêm '$item' vào hàng đợi.")
end

# Hàm loại bỏ phần tử khỏi hàng đợi
function dequeue!(q::Queue)
    if !isempty(q.elements)
        item = popfirst!(q.elements)  # Loại bỏ phần tử đầu tiên
        println("Đã lấy '$item' ra khỏi hàng đợi.")
        return item
    else
        println("Hàng đợi trống!")
        return nothing
    end
end

# Hàm xem phần tử ở đầu hàng đợi
function front(q::Queue)
    if !isempty(q.elements)
        return first(q.elements)  # Truy cập phần tử đầu tiên
    else
        println("Hàng đợi trống!")
        return nothing
    end
end

# Hàm kiểm tra hàng đợi rỗng
function is_empty(q::Queue)
    return isempty(q.elements)
end

# Hàm in nội dung hàng đợi
function display(q::Queue)
    println("Hàng đợi (đầu đến cuối): ", collect(q.elements))
end

# Minh họa sử dụng hàng đợi với Deque
function main()
    queue = Queue()
    enqueue!(queue, "Tài Liệu 1")
    enqueue!(queue, "Tài Liệu 2")
    enqueue!(queue, "Tài Liệu 3")
    display(queue)  # Output: Hàng đợi (đầu đến cuối): ["Tài Liệu 1", "Tài Liệu 2", "Tài Liệu 3"]
    front_item = front(queue)
    println("Phần tử ở đầu hàng đợi: ", front_item)  # Output: Tài Liệu 1
    dequeue!(queue)
    display(queue)  # Output: Hàng đợi (đầu đến cuối): ["Tài Liệu 2", "Tài Liệu 3"]
    println("Hàng đợi có trống không? ", is_empty(queue) ? "Có" : "Không")  # Output: Không
end

main()
