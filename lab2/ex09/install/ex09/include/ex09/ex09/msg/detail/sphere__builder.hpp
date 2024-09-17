// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ex09:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef EX09__MSG__DETAIL__SPHERE__BUILDER_HPP_
#define EX09__MSG__DETAIL__SPHERE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ex09/msg/detail/sphere__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ex09
{

namespace msg
{

namespace builder
{

class Init_Sphere_radius
{
public:
  explicit Init_Sphere_radius(::ex09::msg::Sphere & msg)
  : msg_(msg)
  {}
  ::ex09::msg::Sphere radius(::ex09::msg::Sphere::_radius_type arg)
  {
    msg_.radius = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ex09::msg::Sphere msg_;
};

class Init_Sphere_center
{
public:
  Init_Sphere_center()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Sphere_radius center(::ex09::msg::Sphere::_center_type arg)
  {
    msg_.center = std::move(arg);
    return Init_Sphere_radius(msg_);
  }

private:
  ::ex09::msg::Sphere msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ex09::msg::Sphere>()
{
  return ex09::msg::builder::Init_Sphere_center();
}

}  // namespace ex09

#endif  // EX09__MSG__DETAIL__SPHERE__BUILDER_HPP_
