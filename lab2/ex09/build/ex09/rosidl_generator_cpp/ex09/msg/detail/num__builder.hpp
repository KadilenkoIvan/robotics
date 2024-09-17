// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ex09:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef EX09__MSG__DETAIL__NUM__BUILDER_HPP_
#define EX09__MSG__DETAIL__NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ex09/msg/detail/num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ex09
{

namespace msg
{

namespace builder
{

class Init_Num_num
{
public:
  Init_Num_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ex09::msg::Num num(::ex09::msg::Num::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ex09::msg::Num msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ex09::msg::Num>()
{
  return ex09::msg::builder::Init_Num_num();
}

}  // namespace ex09

#endif  // EX09__MSG__DETAIL__NUM__BUILDER_HPP_
