// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ex09:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef EX09__MSG__DETAIL__NUM__STRUCT_H_
#define EX09__MSG__DETAIL__NUM__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Num in the package ex09.
typedef struct ex09__msg__Num
{
  int64_t num;
} ex09__msg__Num;

// Struct for a sequence of ex09__msg__Num.
typedef struct ex09__msg__Num__Sequence
{
  ex09__msg__Num * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ex09__msg__Num__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // EX09__MSG__DETAIL__NUM__STRUCT_H_
